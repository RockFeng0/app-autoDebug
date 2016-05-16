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

x = XmlDpc(r'D:\auto\python\app-autoDebug\data\tt.xml')
x.setFeature()
print x.classifyFeatureAll()
    