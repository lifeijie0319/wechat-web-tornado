import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import backref, relationship

from .base import Base


class SignInRule(Base):
    '''
    累计签到规则
    '''
    __tablename__ = 'SIGN_IN_RULE'

    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    credits = Column(Integer, nullable=False)
    remark = Column(Text)


class SignInRecord(Base):
    '''
    签到数据
    '''
    __tablename__ = 'SIGN_IN_RECORD'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('USER.id'))
    insert_dtime = Column(DateTime, default=datetime.datetime.now)
    credits = Column(Integer, nullable=False)

    user = relationship('User', backref='signin_records')
