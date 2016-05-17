# -*- encoding: utf-8 -*-
'''
Current module: halou.myxlsx

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      halou.myxlsx,v 1.0 2016年5月16日
    FROM:   2016年5月16日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from pyrunner.automation.datatrans import ExcelDpc

x = ExcelDpc(r'D:\auto\python\app-autoDebug\data\tt.xlsx')

step_feature=["Steps","PreCommand","Head","Data","PostCommand"]
info_feature=["TestCaseID","Description","Verify"]
unique="TestCaseID"

x.setXlsCasesFeature(sheet="Sheet1",unique="A",info_feature=["B"],step_feature=["C"])
print x.getXlsCasesValue()

x.setXlsCasesFeature(sheet="Sheet1",unique="A",info_feature=[],step_feature=[])
print x.getXlsCasesValue()

