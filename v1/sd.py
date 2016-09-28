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

import sc
import sys,os,types

from pyrunner.executer import tracer
def get_exe_path(proj_name):
    lib_path = os.path.abspath(sys.path[0])
    return os.path.join(lib_path,proj_name).decode("cp936")
tracer.set_proj_path(sc.PROJ_NAME, get_exe_path(sc.PROJ_NAME), sysencoding = False)
 
from pyrunner.automation.datatrans import ExcelDpc,XmlDpc
from pyrunner.executer import RunXlsxDpcData
from pyrunner.common import p_env

class DataDriverMap(ExcelDpc):
    '''
    data = DataDriverMap('D:\\auto\\python\\app-autoDebug\\appDebugProject\\data\\tt.xlsx')
    testSet = data.getMapDataFeature()
    
    for (tid, test) in testSet.items():
        print '\n', tid
        for (k, v) in test.items():
            print '\t---%s:: %s' % (k, v)
    '''
    
    def __init__(self,xls_file, **kwargs):
        ExcelDpc.__init__(self, xls_file)
        self.setDetailFeature(**kwargs)     
        self.__setDataFeature()
                
    def getMapDataFeature(self):
        datas = self.__getDataFeature()
        return datas
    
    def setDetailFeature(self,**kwargs):
        # default feature
        self.__feature = {"sheet" : "TestCase",
                          "step" : ["Steps","PreCommand","Head","Data","PostCommand"],
                          "info" : ["TestCaseID","Description","Verify","StepDescription","Tester"],
                          "unique" : "TestCaseID" 
                          }
        
        # update
        for k,v in kwargs.items():
            if k in self.__feature:
                self.__feature.update({k:v})
        
        
    def getDetailFeature(self):
        return self.__feature
    
    def __getDataFeature(self):
        return self.getXlsCasesValue()
        
    def __setDataFeature(self):
        self.setXlsCasesFeature(sheet = self.__feature["sheet"],
                                step_feature = self.__feature["step"],
                                info_feature = self.__feature["info"],
                                unique = self.__feature["unique"])


class ElemFeatureXML(XmlDpc):
    '''
    ef = ElemFeatureXML(r"D:\auto\python\app-autoApp\demoProject\data\sysweb.xml")    
    result = ef.getFeature(["Login","LoginAccountInput"])
    print ef.getClasses()
    '''
    def __init__(self,file_path, **kwargs):
        if not os.path.isfile(file_path):
            raise Exception("Invalid xml file: '%s'" %file_path)
        XmlDpc.__init__(self,file_path)
        self.setDetailFeature(**kwargs)
        self.__setUIFeature()
        
    def getClasses(self):
        return self.classifyFeatureAll()
    
    def setDetailFeature(self,**kwargs):
        # default feature
        self.__feature = {"fstr" : ["by","value"],
                          "fint" : ["index"],
                          "fattr": [],
                          "top" : "root",
                          "bottom" : "by" ,
                          "fclass" : "Web",
                          }
        # update
        for k,v in kwargs.items():
            if k in self.__feature:
                self.__feature.update({k:v})
    
    def getDetailFeature(self):
        return self.__feature    
    
    def __setUIFeature(self):
        self.setFeature(str_feature = self.__feature["fstr"],
                        int_feature = self.__feature["fint"],
                        attr_feature = self.__feature["fattr"],
                        class_feature = self.__feature["fclass"],
                        root_tag = self.__feature["top"],
                        feature_tag = self.__feature["bottom"],
                        )

# def get_debug_path(proj_name, debug = True):
#     ''' Parameter:
#             proj_name - a project director name, "debug" etc. 
#     '''
#     if debug:
#         #调试路径
#         return os.path.join(os.path.dirname(os.path.abspath(sys.path[0])),proj_name)
#     else:
#         return os.path.join(os.path.abspath(sys.path[0]),proj_name).decode("cp936")

def judgement(resp, err_msg, case_id = None, resp_form = ("RST", "ACTUAL", "EXPT", "DES")):
    ''' Parameter:
        resp - a case or a case step result
        err_msg - if not None, means the case or case step has error, when running a case or a case step.  
        case_id - if not None, means the 'resp' is the case step result to judge. if None, means the 'resp' is the whole case result to judge.
        resp_form - when case_id is not None, it defines the critical formation of 'resp'
    '''    
    test_next = True
    # judge execution err_msg and resp format
    if err_msg:
        err_info = err_msg        
    elif not case_id and not isinstance(resp, (types.TupleType,types.ListType)):
        err_info = "\tInvalid format: argument #1 must support iteration"
    else:
        err_info = None

    if err_info:
        test_next = False
        print "Error-step: %s" %err_info 
        tracer.error(err_info)
             
    elif case_id:
        # judge case step resp
        if resp:
            tracer.ok("\tStep pass.")            
            print "Pass-step"
        else:
            test_next = False
            tracer.fail("\tStep fail.")            
            print "Fail-step"            
    else:
        # judge case resp
        rst = dict(zip(resp_form, resp))
        tracer.normal("\t实际测试结果：[%s]" %(rst.get("ACTUAL")))        
        if rst.get("RST"):
            tracer.ok("\tVerify complete.[%s]" %rst.get("DES"))
            print "Pass-verify"
        else:
            test_next = False
            tracer.normal("期望测试结果：[%s]" %(rst.get("EXPT")))
            tracer.fail("Verify complete.[%s]" %rst.get("DES"))        
            print "Fail-verify"
    return test_next
    
class SdRunner:
    def __init__(self,section, debug = False):
        self.itemrst = None
        
    def set_feature(self, test_excel_name, **kwargs):
        feature_driver = DataDriverMap(os.path.join(p_env.CASE_PKG_PATH, test_excel_name), **kwargs)
#         feature_driver = DataDriverMap(os.path.join(p_env.DATA_PATH, test_excel_name), **kwargs)
        self.testFeature = feature_driver.getDetailFeature()       
        self.testSet = feature_driver.getMapDataFeature()
    
    def start_run(self, mname, caseid = None):
        if isinstance(mname, types.ModuleType):
            module = mname
        else:
            module_names = {"web":"UIWeb","pc":"UIPc","pad":"UIPad","key":"KeyClasses"}
            if not mname in module_names:
                raise Exception("Need specify web/pc/pad/key. not '%s'" %mname)
            module = __import__(module_names.get(mname))
        
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
            
            if not judgement(test_result[0], test_result[1], caseid):
                self.itemrst = (None,False)
                break
            
            if not caseid:                
                self.itemrst = (caseid,p_env.CASE_PASS)

if __name__ == "__main__":
    a = SdRunner("env241", debug = True)    
    a.set_feature("tt.xlsx",info=["TestCaseID","Description","Verify","StepDescription","Tester", "CaseType"])
    print a.testFeature
    print a.testSet
    a.start_run("key", caseid = "1")
    
    
    