# -*- encoding: utf-8 -*-
'''
Current module: mytestxlsx

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      mytestxlsx,v 1.0 2016年5月16日
    FROM:   2016年5月16日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

# import sys
# sys.path.append(r'D:\auto\python\app-autoApp')

from pyrunner.executer import RunXlsxDpcData
from testcase import test_run_xlsx

xls_dpc_testcases = {'ATP-3': {'head': {'Step_1_info': '{"prepareLogin":["X-PC-Authenticate-key: AAAAAAAAAA","X-Device-Id: B8AEED2FE3E0","X-Device-Type: 4"]}'}, 'description': '\xe8\x87\xaa\xe5\x8a\xa8\xe7\x99\xbb\xe5\xbd\x95\xe6\x95\x99\xe5\xad\xa6\xe4\xb8\xad\xe5\xbf\x83', 'precommand': {'Step_1_info': {}, 'Step_2_info': {}}, 'verify': 'Contain("\\"resultCode\\":0")', 'postcommand': {'Step_1_info': 'action_set_for_http("prepareLogin",user_account=DyData("userAccount"))', 'Step_2_info': 'action_set_for_http("prepareLogin",user_name=DyData("userInfo"))'}, 'steps': {'Step_1_info': 'action_set_for_http("prepareLogin")', 'Step_2_info': 'action_get_for_http("http://192.168.102.102:8002/portal/ClientApi/prepareLogin")'}, 'data': {'Step_1_info': '{"prepareLogin":{"loginId":glob.vars["lg_id"],"userId":glob.vars["cpi"][0],"staticPassword":glob.vars["cpi"][1]}}'}}}

executer    = RunXlsxDpcData(xls_dpc_testcases)
status      = executer.start();# status是个迭代器，start函数，返回(关键字函数,用例编号)
for fs,caseid in status:
    test_result = executer(test_run_xlsx).call(fs)
    if caseid == None:
        executer.judgement(test_result, fs,u"看，飞机，飞机，飞机！！！")
        
    
