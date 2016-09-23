# -*- encoding: utf-8 -*-
'''
Current module: pub

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      pub,v 1.0 2016年9月23日
    FROM:   2016年9月23日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
import os,sys,types
import sc
from pyrunner.executer import tracer

def set_path():
    fp = os.path.abspath(sys.path[0])
    if os.path.isfile(fp):
        fp = os.path.dirname(fp)
        
    path = os.path.join(fp, sc.PROJ_NAME).decode("cp936")    
    tracer.set_proj_path(sc.PROJ_NAME, path, sysencoding = False)

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