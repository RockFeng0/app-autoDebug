# -*- encoding: utf-8 -*-
'''
Current module: halou.myxml

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      halou.myxml,v 1.0 2016年5月16日
    FROM:   2016年5月16日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from pyrunner.automation.datatrans import XmlDpc


# x = XmlDpc(r'D:\auto\python\app-autoDebug\data\tt.xml')
x = XmlDpc(r'D:\auto\python\app-autoDebug\data\test.xml')
x.setFeature(str_feature=["by","value"],
             int_feature=["index"],
             class_feature="Test",
             root_tag='root',
             feature_tag='by',
             attr_feature = ["className","resourceId"])

result = x.classifyFeatureAll()

'''
# result 的值：
class Login:
    @classmethod
    class LoginAccountInput(Test):
        by = 'id'
        value = 'login_text_username-input'
        uiselector = {}
    @classmethod
    class LoginPasswordInput(Test):
        by = 'id'
        value = 'login_text_password-input'
        uiselector = {}
    @classmethod
    class LoginCheckCode(Test):
        by = 'id'
        value = 'login_text_checkcode-input'
        uiselector = {}
    @classmethod
    class LoginStartButton(Test):
        index = 0
        by = 'xpath'
        value = '//button'
        uiselector = {}
    @classmethod
    class LoginErrorTipText(Test):
        by = 'id'
        value = 'x-auto-17-content'
        uiselector = {}
    @classmethod
    class LoginErrorTipBtn(Test):
        index = 2
        by = 'css selector'
        value = 'button'
        uiselector = {'className': u'textview', 'resourceId': u'edt_account'}
'''
class Test:
    @classmethod
    def Hello(cls):
        print "Hello World."

exec(result)

def getObjFromXmlMap(seq):
    '''Sample:
        obj = getObjFromXmlMap(["Login","LoginAccountInput"])
        obj.type("username1")
    '''
    return eval(".".join(seq))

if __name__ == "__main__":
    obj = getObjFromXmlMap(["Login","LoginAccountInput"])
    obj.Hello()
    print obj.by
    print obj.value
    
    



