# -*- encoding: utf-8 -*-
'''
Current module: sd

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      sd,v 1.0 2016年9月18日
    FROM:   2016年9月18日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import os,types
import de,pub
from pyrunner.executer import RunXlsxDpcData,tracer
from pyrunner.common import p_env

pub.set_path()
class SdRunner:
    def __init__(self,section, debug = False):
        self.itemrst = None
        
    def set_feature(self, test_excel_name, **kwargs):
        feature_driver = de.DataDriverMap(os.path.join(p_env.CASE_PKG_PATH, test_excel_name), **kwargs)
#         feature_driver = DataDriverMap(os.path.join(p_env.DATA_PATH, test_excel_name), **kwargs)
        self.testFeature = feature_driver.getDetailFeature()       
        self.testSet = feature_driver.getMapDataFeature()
                                
    def start_run(self,mname, caseid = None):
                       
        if isinstance(mname, types.ModuleType):
            module = mname
        else:
            module = __import__(mname)
        
        test_cases = {}
        if caseid:
            case = self.testSet.get(caseid)
            if not case:
                print "Warning: do not hava case-> %r" %caseid                
                return
            test_cases[caseid] = case
        else:
            test_cases = self.testSet
        
        self.executer    = RunXlsxDpcData(test_cases, debug = tracer.debug)
        status = self.executer.start()        
        for fs,caseid in status:
            self.itemrst = (caseid,None)            
            test_result = self.executer(module).queue(fs)
            
            if not pub.judgement(test_result[0], test_result[1], caseid):
                self.itemrst = (None,False)
                break
            
            if not caseid:                
                self.itemrst = (caseid,p_env.CASE_PASS)
    
    def get_dcase(self,caseid):
        test_cases = {}
        if caseid:
            case = self.testSet.get(caseid)
            if not case:
                print "Warning: do not hava case-> %r" %caseid             
                return
            test_cases[caseid] = case
        else:
            test_cases = self.testSet
        return test_cases
        
if __name__ == "__main__":
    a = SdRunner("env241", debug = True)    
    a.set_feature("tt.xlsx",info=["TestCaseID","Description","Verify","StepDescription","Tester", "CaseType"])
    print a.testFeature
    print a.testSet.get("a1")
    a.start_run("UIWeb",caseid = "a1")
    
    
    