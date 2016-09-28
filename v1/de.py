# -*- encoding: utf-8 -*-
'''
Current module: de

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      de,v 1.0 2016年9月23日
    FROM:   2016年9月23日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from pyrunner.automation.datatrans import ExcelDpc

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