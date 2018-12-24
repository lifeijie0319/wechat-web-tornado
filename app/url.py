#-*- coding:utf-8 -*-
import os

from tornado.web import StaticFileHandler

from . import config
from .view import common
from .view import form
from .view import signin
from .view import wx


url_patterns = [
    (r'/wxdemo', common.RootHandler),
    (r'/wxdemo/([^/]+\.[^/]+)', StaticFileHandler, {'path': config.MEDIA_PATH}),
    (r'/wxdemo/media/(.*)', StaticFileHandler, {'path': config.MEDIA_PATH}),
    (r'/wxdemo/staticfile/(.*)', common.StaticTPLHandler),
    (r'/wxdemo/test/(?P<action>\w+)', common.TestHandler),
    (r'/wxdemo/common/send_vcode', common.SendVcodeHandler),
    (r'/wxdemo/common/refresh_pic_vcode', common.RefreshPicVcodeHandler),
    (r'/wxdemo/common/upload_img', common.UploadImgHandler),
    (r'/wxdemo/wx/jssdk', wx.JSSDKHandler),
    (r'/wxdemo/wx/refresh_token', wx.RefreshTokenHandler),
    (r'/wxdemo/wx/refresh_menu', wx.RefreshMenuHandler),
    (r'/wxdemo/wx/upload_img', wx.UploadImgHandler),
    (r'/wxdemo/form', form.FormHandler),
    (r'/wxdemo/signin', signin.SignInHandler),
]
