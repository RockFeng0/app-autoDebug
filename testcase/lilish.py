# -*- coding: utf-8 -*-
from kilofar.uimap import *


def lili_1():
    # start
    SDKAndroid.WaitForConnection()    
    component = "sh.lilith.dgame.DK/sh.lilith.dgame.DGame"
    SDKAndroid.LaunchApp(component)
    print "launch app ok"
    
def lili_2():
    text = LoginUI.DuoKu.GetText()
    if text == "多酷登录":
        LoginUI.Baidu.Touch()
    Login.Username.TypeInClear("1234")
    Login.Password.TypeInClear("3333")        
    Login.Ok.Touch()
    print "login action complete"
    
def lili_3():
    Main.Goin.Touch()
    print "Go in ?"

def before_each_testcase():
    pass
    

def after_each_testcase():
    pass


print "start"