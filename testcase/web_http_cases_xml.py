# -*- encoding: utf-8 -*-
'''
Current module: twsm.testcase.test_case_one

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:     luokefeng@twsm.com.cn
    RCS:      twsm.testcase.test_case_one,v 1.0 2015年5月14日
    FROM:   2015年5月14日
********************************************************************
            Copyright (c) 2015-2020  天闻数媒有限公司
======================================================================

Provide a function for the test of web services

'''


from com.twsm_integration import TwsmIntegraion
import re
from pyrunner import p_log


def TestCase001_ATP_1():
    # 定义
    
    product = "test"
    interface = "getPublishResultList"    
    test_case = "ATP-1"
    expect_result = "NBZDCS2600000000000"
    
    # 执行--出于演示目的，所有输出，都会打印出来    
    p_log.step_info("step", "step_1,发送请求: 产品 %s 接口  %s 编号 %s " %(product,interface,test_case))
    twsm_obj.twsm_post_xml_http(product, interface, test_case)    
    
    # 期望结果的判断
    p_log.step_info("step", "step_2,验证请求结果 ")
    prog = re.compile(r'"publishId":"(\w*)"')
    m = prog.search(twsm_obj.buf_string)
    if m:    
        if m.group(1) == expect_result:
            print "%s test: Ok." %(test_case)
            p_log.step_info("pass", "step_3,通过 ")
        else:
            print "%s test: Fail.('%s' not match '%s')" %(test_case,m.group(1),expect_result)
            p_log.step_info("fail", "step_3,失败,期望 : %s  实际：%s " %(expect_result,m.group(1)))
    else:
        print "%s test: Fail.(not find '%s')" %(test_case,expect_result)
        p_log.step_info("fail", "step_3,失败,期望 : %s  实际：%s " %(expect_result,m.group(1)))



def TestCase002_ATP_2():
    # 定义    
    product = "test"
    interface = "getPublishResultList"    
    test_case = "ATP-2"
    expect_result = "NBZDCS2600000000002"
    
    # 执行--出于演示目的，所有输出，都会打印出来    
    p_log.step_info("step", "step_1,发送请求: 产品 %s 接口  %s 编号 %s " %(product,interface,test_case))
    twsm_obj.twsm_post_xml_http(product, interface, test_case)    
    
    # 期望结果的判断
    p_log.step_info("step", "step_2,验证请求结果 ")
    prog = re.compile(r'"publishId":"(\w*)"')
    m = prog.search(twsm_obj.buf_string)
    if m:    
        if m.group(1) == expect_result:
            print "%s test: Ok." %(test_case)
            p_log.step_info("pass", "step_3,通过 ")
        else:
            print "%s test: Fail.('%s' not match '%s')" %(test_case,m.group(1),expect_result)
            p_log.step_info("fail", "step_3,失败,期望 : %s  实际：%s " %(expect_result,m.group(1)))
    else:
        print "%s test: Fail.(not find '%s')" %(test_case,expect_result)
        p_log.step_info("fail", "step_3,失败,期望 : %s  实际：%s " %(expect_result,m.group(1)))

def TestCase003_ATP_3():
    # 定义    
    product = "test"
    interface = "getPublishResultList"
    test_case = "ATP-3"
    expect_result = "NBZDCS2600000000002"
    
    # 执行--出于演示目的，所有输出，都会打印出来    
    p_log.step_info("step", "step_1,发送请求: 产品 %s 接口  %s 编号 %s " %(product,interface,test_case))
    twsm_obj.twsm_post_xml_http(product, interface, test_case)    
    
    # 期望结果的判断
    p_log.step_info("step", "step_2,验证请求结果 ")
    prog = re.compile(r'"publishId":"(\w*)"')
    m = prog.search(twsm_obj.buf_string)
    if m:    
        if m.group(1) == expect_result:
            print "%s test: Ok." %(test_case)
            p_log.step_info("pass", "step_3,通过 ")
        else:
            print "%s test: Fail.('%s' not match '%s')" %(test_case,m.group(1),expect_result)
            p_log.step_info("fail", "step_3,失败,期望 : %s  实际：%s " %(expect_result,m.group(1)))
    else:
        print "%s test: Fail.(not find '%s')" %(test_case,expect_result)
        p_log.step_info("fail", "step_3,失败,期望 : %s  实际：%s " %(expect_result,m.group(1)))

def before_each_testcase():
    global twsm_obj
    cfg_section = "twsm2"
    p_log.step_info("normal", "使用配置  %s " %cfg_section)
    twsm_obj=TwsmIntegraion(cfg_section)

def after_each_testcase():
    pass




'''
# 未注册设备
a.twsm_post_xml_http("test", "getPublishResultList", "test-1")
# 未鉴权用户
a.twsm_post_xml_http("test", "getPublishResultList", "test-2")
# 成功响应
a.twsm_post_xml_http("test", "getPublishResultList", "test-3")

# 演示 ATP-1
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-1")
    
# 演示ATP-2
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-2")

# 演示ATP-3
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-3")

# 演示ATP-4
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-4")

# 演示ATP-5
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-5")

# 演示ATP-6
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-6")

# 演示ATP-7
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-7")

# 演示ATP-8
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-8")

# 演示ATP-9
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-9")

# 演示ATP-10
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-10")

# 演示ATP-11
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-11")

# 演示ATP-12
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-12")

# 演示ATP-13
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-13")

# 演示ATP-14
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-14")

# 演示ATP-15
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-15")

# 演示ATP-16
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-16")

# 演示ATP-17
a.twsm_post_xml_http("test", "getPublishResultList", "ATP-17")
'''
    