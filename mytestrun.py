# -*- encoding: utf-8 -*-
'''
Current module: mytestrun

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      mytestrun,v 1.0 2016年5月6日
    FROM:   2016年5月6日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

# import sys
# sys.path.append(r'D:\auto\python\app-autoApp')

from pyrunner.executer import RunModule

executer    = RunModule("test_run_module")
status      = executer.start();# status是个迭代器，start函数，返回(测试结果,用例名称)

for rs,case_name in status:
    print "Judging the case['%s'] result" %case_name
    executer.judgement(rs)
    
    


