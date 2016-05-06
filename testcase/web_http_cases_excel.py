# -*- encoding: utf-8 -*-
'''
Current module: twsm.testcase.web_http_cases_excel

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:     luokefeng@twsm.com.cn
    RCS:      twsm.testcase.web_http_cases_excel,v 1.0 2015年5月19日
    FROM:   2015年5月19日
********************************************************************
            Copyright (c) 2015-2020  天闻数媒有限公司
======================================================================

Provide a function for the test of web services

'''

from com.twsm_integration import TwsmIntegraion
import re
from pyrunner import p_log

def TestCase_In_Excel_ATP_1():
    sheet = "Sheet1"
    test_case_id = "ATP-1"
   
    twsm_obj.twsm_post_xls_http(sheet,test_case_id)

def TestCase_In_Excel_ATP_2():
    sheet = "Sheet1"
    test_case_id = "ATP-2"
   
    twsm_obj.twsm_post_xls_http(sheet,test_case_id)

def before_each_testcase():
    global twsm_obj
    cfg_section = "twsm2"
    p_log.step_info("normal", "使用配置  %s " %cfg_section)
    twsm_obj=TwsmIntegraion(cfg_section)

def after_each_testcase():
    pass
