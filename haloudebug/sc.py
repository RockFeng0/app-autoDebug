# -*- encoding: utf-8 -*-
'''
Current module: haloudebug.sc

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      haloudebug.sc,v 1.0 2016年8月29日
    FROM:   2016年8月29日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

TITLE = u"HaLouDebugger Tools"

MENUS = [
         {u"文件": [u"加载用例"]},
         {u"编辑": [u"调试选中",u"清除选中",u"清空列表"]},
         {u"执行": [u"已选的用例",u"加载的用例",u"配置的用例",u"停运后续用例"]},
         {u'查看': [u"刷新日志",u"控制台日志",u'测试报告']},
         {u"帮助": [u"关于"]},  
         ]
CASE = {"caseid":None,
        "casetype":None,
        "tester":None,
        "steps":None,
        "description":None,
        "precommand":None,
        "head":None,
        "data":None,
        "postcommand":None,
        "verify":None,
        }

CASE_ITEMS = []
CASE_SORTED_IDS = []
CASE_MAP = {}

AITEST_CONFIG = {"section":None,
                 "all_excels":[],
                 "caseid":None,
                 "echoall":None,
                 "debug":None,
                 "interrupt":None,
                 "log_file":None, 
                 "excel_name":None,
                 "proj_path":None,      
                 }

RUNNER = None
INTEG = None
DISB = None
STOP = None
RUNNER_LOG_HANDLE = None

TREE = None
TEXTAREA = None
PROCESSBAR = None

