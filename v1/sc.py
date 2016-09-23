# -*- encoding: utf-8 -*-
'''
Current module: sc

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      sc,v 1.0 2016年9月18日
    FROM:   2016年9月18日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
PROJ_NAME = "appDebugProject"

TITLE = u"AiTest自动化测试用例编写工具"

MENUS = [
         {u"文件": [u"加载用例"]},
         {u"编辑": [u"清除选中",u"清空列表"]},
         {u"执行": [u"已选的用例",u"加载的用例",u"配置的用例",u"停运后续用例"]},
         {u'查看': [u"控制台日志",u'测试报告']},
         {u"帮助": [u"关于"]},  
         ]
CASE = {"id":None,"value":{}}
