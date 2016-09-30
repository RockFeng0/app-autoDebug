# -*- encoding: utf-8 -*-
'''
Current module: UIPc

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      UIPc,v 1.0 2016年9月23日
    FROM:   2016年9月23日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import os
from dx import ElemFeatureXML
from pyrunner.common import p_env,p_common

p_common.config = p_common.get_current_config("env241")

try:
    from pyrunner.drivers import WindowP
    path = os.path.join(p_env.DATA_PATH,p_common.config.get("xml_map_win_name"))
    feature = ElemFeatureXML(path,
                             fstr = ["ident"],
                             fint = ["index","timeout"],
                             fclass = "WindowP",
                             toop = "root",
                             bottom = "ident").getClasses()         
    exec(feature)
except:
    pass

# class LoginPC:
# 
#     class TextUserName(WindowP):
# 
#         timeout = 10
# 
#         ident = '{"AutomationId" : "txtUserName"}'
# 
#     class PwdUser(WindowP):
# 
#         ident = '{"AutomationId" : "PwdUser"}'
# 
#     class CkbIsSavePwd(WindowP):
# 
#         ident = '{"AutomationId" : "ckbIsSavePwd"}'
# 
#     class BtnLogin(WindowP):
# 
#         ident = '{"AutomationId" : "BtnLogin"}'
        
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