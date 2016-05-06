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
import sys,os
os.system("chcp 437")
sys.path.append(r'D:\auto\python\app-autoDebug')
sys.path.append(r'C:\Python27\Lib\site-packages\pyrunner-1.0.0-py2.7.egg')
sys.path.append(r'C:\Python27\Lib')


from kilofar import runner

runner.run_testcases("lilishconf", "lilish")