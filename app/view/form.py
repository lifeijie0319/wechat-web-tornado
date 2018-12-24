#-*- coding:utf-8 -*-
import json

from tornado.log import app_log

from .common import BaseHandler


class FormHandler(BaseHandler):
    def get(self):
        self.render('form.html')

    def post(self):
        app_log.info(self.request.body)
        data = json.loads(self.request.body)
        vcode = data.get('vcode')
        real_vcode = self.get_secure_cookie('vcode')
        app_log.info('real_vcode %s', real_vcode)
        if not real_vcode:
            self.write({'success': False, 'msg': '验证码过期'})
            return
        if vcode != real_vcode:
            self.write({'success': False, 'msg': '验证码错误'})
            return
        self.write({'success': True})
