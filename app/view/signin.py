#-*- coding:utf-8 -*-
import datetime
import json

from sqlalchemy import extract
from tornado.gen import coroutine
from tornado.log import app_log

from .common import BaseHandler, need_openid, need_reg
from ..db.model import SignInRecord, SignInRule
from ..tool import gen_req_token, G


class SignInHandler(BaseHandler):
    @need_openid
    @need_reg
    @coroutine
    def get(self):
        app_log.info('FINAL OPENID: %s', self.openid)
        init = self.get_arguments('init')
        app_log.info('init?%s', init)
        if init and init[0] == 'true':
            now = datetime.datetime.now()
            signed_records = G.db.query(SignInRecord).filter(SignInRecord.user==self.user)\
                .filter(extract('year', SignInRecord.insert_dtime)==now.year)\
                .filter(extract('month', SignInRecord.insert_dtime)==now.month).all()
            signed_dates_index = [signed_record.insert_dtime.day - 1 for signed_record in signed_records]
            all_gift_credits = sum([signed_record.credits for signed_record in signed_records])
            today_is_signed = 'true' if (now.day - 1) in signed_dates_index else 'false'
            self.write({'signed_dates': signed_dates_index, 'credits': all_gift_credits, 'today_is_signed': today_is_signed})
            return
        rules = G.db.query(SignInRule).all()
        context = {
            'rules': rules,
            'credits': self.user.credits,
            'req_token': gen_req_token(),
        }
        self.render('signin.html', **context)

    @coroutine
    def post(self):
        now = datetime.datetime.now()
        today_is_signed = G.db.query(SignInRecord).filter(SignInRecord.user==self.user)\
            .filter(extract('year', SignInRecord.insert_dtime)==now.year)\
            .filter(extract('month', SignInRecord.insert_dtime)==now.month)\
            .filter(extract('day', SignInRecord.insert_dtime)==now.day).count()
        if today_is_signed:
            self.write({'success': False, 'msg': u'今天已经签过到,一天只能签到一次'})
            return
        added_credits = self.calcu_gift_credits(now)
        record = SignInRecord(user=user, credits=added_credits)
        try:
            G.db.add(record)
            self.user.credits += added_credits
        except:
            G.db.rollback()
        else:
            G.db.commit()
        context = {
            'success': True,
            'today_index': now.day,
            'added_credits': added_credits,
            'new_credits': self.user.credits,
        }
        self.write(context)

    def calcu_gift_credits(self, now):
        base_gift_credits = 2
        rules = G.db.query(SignInRule).all()
        signed_days = G.db.query(SignInRecord).filter(SignInRecord.user==self.user)\
            .filter(extract('year', SignInRecord.insert_dtime)==now.year)\
            .filter(extract('month', SignInRecord.insert_dtime)==now.month).count()
        ex_gift_credits = 0
        for rule in rules:
            if rule.day == signed_days:
                ex_gift_credits = rule.credits
                break
        return base_gift_credits + ex_gift_credits
