# -*- encoding: utf-8 -*-
'''
Current module: kilofar.datamap

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      kilofar.datamap,v 1.0 2016年5月6日
    FROM:   2016年5月6日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import os
from pyrunner.automation.datatrans import XmlDpc

class XmlFeatureMap(XmlDpc):

    def __init__(self,file_path):
        if not os.path.isfile(file_path):
            raise Exception("Invalid xml file: '%s'" %file_path)
        XmlDpc.__init__(self,file_path)
        self.__setAppFeature()
                
    def getClasses(self):
        return self.classifyFeatureAll()
    
    def __setAppFeature(self):
        str_feature=["by","value"]#;设置字符型的数据节点
        int_feature=["timeout"];#设置数字型的数据节点，
        class_feature="SDKApp";#设置 继承的 类
        root_tag='root';# 设置，遍历开始的 节点
        feature_tag='by';# 设置，遍历结束的节点，该节点的兄弟节点会遍历
        self.setFeature(str_feature,int_feature,class_feature,root_tag,feature_tag)

if __name__ == "__main__":
    ef = XmlFeatureMap(r"D:\auto\python\app-autoApp\demoProject\data\sysapp_hierarchy.xml")    
    result = ef.getFeature(["Login","LoginAccountInput"])
    print result
    print ef.getClasses()
    
    