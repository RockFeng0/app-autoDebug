# -*- encoding: utf-8 -*-
'''
Current module: KeyClasses

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      KeyClasses,v 1.0 2016年9月18日
    FROM:   2016年9月18日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import os
from sd import ElemFeatureXML
from pyrunner.common import p_env,p_common

p_common.config = p_common.get_current_config("env241")
try:
    from pyrunner.drivers import Web,Browser
    path = os.path.join(p_env.DATA_PATH,p_common.config.get("xml_map_web_name"))
    feature = ElemFeatureXML(path,
                             fstr = ["by", "value"],
                             fint = ["index"],
                             fattr = [],
                             top = "root",
                             bottom = "by",
                             fclass = "Web").getClasses()
    exec(feature)
except:
    pass

# class Login:
#     class LoginAccountInput(Web):
#         by = 'id'
#         value = 'login_text_username-input'
#     class LoginPasswordInput(Web):
#         by = 'id'
#         value = 'login_text_password-input'
#     class LoginCheckCode(Web):
#         by = 'id'
#         value = 'login_text_checkcode-input'
#     class LoginStartButton(Web):
#         index = 0
#         by = 'xpath'
#         value = '//button'
#     class LoginErrorTipText(Web):
#         by = 'id'
#         value = 'x-auto-17-content'
#     class LoginErrorTipBtn(Web):
#         index = 2
#         by = 'css selector'
#         value = 'button'
        
class Result:
    '''
    result should be format:
        ("RST", "ACTUAL", "EXPT", "DES")
    '''
    
    @classmethod
    def VerifyContain(cls,des,expect,actual):                
        if expect in actual:
            result = (True,actual,expect,des)
            print "Test[%s] is Pass" %des
        else:
            result = (False,actual,expect,des)
            print "Test[%s] is Fail" %des
        return result
    
    @classmethod
    def VerifyMatch(cls,des,expect,actual):
        if expect == actual:
            result = (True,actual,expect,des)
            print "%s is Pass" %des
        else:
            result = (False,actual,expect,des)
            print "%s is Fail" %des
        return result
    
    @classmethod
    def Normal(cls,des):
        return (True,"","",des)
    