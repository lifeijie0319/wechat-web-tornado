#-*- coding:utf-8 -*-
import base64
import os
import uuid


tornado_settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'tpl'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'static_url_prefix': '/wxdemo/static/',
    'cookie_secret': 'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=',#base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    'xsrf_cookies': True,
    'debug': True,
}
BASE_URL = 'https://hz.wx.yinsho.com/wxdemo'
REG_URL = BASE_URL + '/staticfile/register.html'
URL_PREFIX = '/wxdemo'
TOKEN = 'yinshowxtoken'
APPID = 'wx6502e1ff74d2a5bd'
APPSECRET = 'e48d375eef7f6af4867fd8953ca6cf91'
ACCESS_TOKEN_KEY = 'demo_access_token'
JSAPI_TICKET_KEY = 'demo_jsapi_ticket'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = BASE_URL + '/media'
MEDIA_PATH = os.path.join(os.path.dirname(__file__), 'media')
REDIS = {
    'HOST': 'localhost',
    'PORT': '6379',
}
MENU={
    'button': [
        {
            'name': '菜单一',
            'sub_button': [
                {
                    'type': 'click',
                    'name': '回复图文消息',
                    'key': 'reply_news',
                },
                {
                    'type': 'click',
                    'name': '回复模板消息',
                    'key': 'reply_tpl',
                },
                {
                    'type': 'click',
                    'name': '客服消息',
                    'key': 'custom_msg',
                },
                #{
                #    'type': 'click',
                #    'name': '汽车分期',
                #    'key': '1',
                #},
                #{
                #    'type': 'click',
                #    'name': '财富管理',
                #    'key': '1',
                #},
            ]
        },
        {
            'name': '菜单二',
            'sub_button': [
                {
                    'type': 'view',
                    'name': '表单',
                    'url': '/staticfile/form.html',
                },
                {
                    'type': 'view',
                    'name': 'jssdk',
                    'url': '/staticfile/jssdk/index.html',
                },
                {
                    'type': 'view',
                    'name': '图片上传',
                    'url': '/staticfile/img_upload.html',
                },
            ]
        },
        {
            'name': '菜单三',
            'sub_button': [
                {
                    'type': 'click',
                    'name': '待定',
                    'key': '1',
                },
                #{
                #    'type': 'click',
                #    'name': '我的账单',
                #    'key': '1',
                #},
                #{
                #    'type': 'click',
                #    'name': '我的额度',
                #    'key': '1',
                #},
                #{
                #    'type': 'click',
                #    'name': '我的积分',
                #    'key': '1',
                #},
                #{
                #    'type': 'view',
                #    'name': '我的客户经理',
                #    'url': '/staticfile/findface.html',
                #},
            ]
        },
    ]
}


class G:pass
