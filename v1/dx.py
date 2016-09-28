# -*- encoding: utf-8 -*-
'''
Current module: dx

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      dx,v 1.0 2016年9月23日
    FROM:   2016年9月23日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
import os
from pyrunner.automation.datatrans import XmlDpc

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