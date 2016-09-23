# -*- encoding: utf-8 -*-
'''
Current module: r_client

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      r_client,v 1.0 2016年9月22日
    FROM:   2016年9月22日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

# import xmlrpclib
# 
# s = xmlrpclib.ServerProxy('http://localhost:8000')
# print s.pow(2,3)  # Returns 2**3 = 8
# 
# # Print list of available methods
# print s.system.listMethods()

class Result:
    '''
    result should be format:
        ("RST", "ACTUAL", "EXPT", "DES")
    '''
    
    @classmethod
    def VerifyContain(cls,des,expect,actual):                
        if expect in actual:
            result = (True,actual,expect,des)
            print "Test[%s] is Pass" %des
        else:
            result = (False,actual,expect,des)
            print "Test[%s] is Fail" %des
        return result
    
    @classmethod
    def VerifyMatch(cls,des,expect,actual):
        if expect == actual:
            result = (True,actual,expect,des)
            print "%s is Pass" %des
        else:
            result = (False,actual,expect,des)
            print "%s is Fail" %des
        return result
    
    @classmethod
    def Normal(cls,des):
        return (True,"","",des)
    