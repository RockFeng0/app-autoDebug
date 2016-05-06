# -*- encoding: utf-8 -*-
'''
Current module: kilofar.uimap

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      kilofar.uimap,v 1.0 2016年5月6日
    FROM:   2016年5月6日
********************************************************************

======================================================================

use MonkeyRunner to run.

'''

import os
from datamap import XmlFeatureMap
from pyrunner.common import p_common,p_env
from pyrunner import SDKAndroid,SDKApp

def get_xml_feature_classes(xml_path=None):
    # xml_path = r'd:\auto\buffer\test.xml'
    path = os.path.join(p_env.DATA_PATH,p_common.config.get("xml_map_class"))
    if xml_path:
        path = xml_path
    feature = XmlFeatureMap(path).getClasses()
    return feature

class Result:
    '''
    result should be format:
        (TEST_DES,TEST_RES,TEST_ACTUAL)    
    '''
    
    @classmethod
    def VerifyContain(cls,des,expect,actual):                
        if expect in actual:
            result = (des,True,actual)
            print "Test[%s] is Pass" %des
        else:
            result = (des,False,actual)
            print "Test[%s] is Fail" %des
        return result
    
    @classmethod
    def VerifyMatch(cls,des,expect,actual):
        if expect == actual:
            result = (des,True,actual)
            print "%s is Pass" %des
        else:
            result = (des,False,actual)
            print "%s is Fail" %des
        return result
    
    @classmethod
    def Normal(cls,des):
        return (des,True)

exec(get_xml_feature_classes()) 

