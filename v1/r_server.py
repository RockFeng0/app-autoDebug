# -*- encoding: utf-8 -*-
'''
Current module: r_server

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      r_server,v 1.0 2016年9月22日
    FROM:   2016年9月22日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
# from SimpleXMLRPCServer import SimpleXMLRPCServer
# 
# 
# # Create server
# server = SimpleXMLRPCServer(("localhost", 8000))
# server.register_introspection_functions()
# 
# # Register pow() function; this will use the value of
# # pow.__name__ as the name, which is just 'pow'.
# server.register_function(pow)
# 
# class MyFuncs:
#     @classmethod
#     class Test:
#         print "test"
#         
# server.register_instance(MyFuncs())
# 
# # Run the server's main loop
# server.serve_forever()
import types
from pyrunner.executer import tracer,RunXlsxDpcData

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

def ttt(test_cases,mname):
    if isinstance(mname, types.ModuleType):
        module = mname
    else:
        module_names = {"web":"UIWeb","pc":"UIPc","pad":"UIPad","key":"KeyClasses","test":"r_client"}
        if not mname in module_names:
            raise Exception("Need specify web/pc/pad/key. not '%s'" %mname)
        module = __import__(module_names.get(mname))
        
    executer    = RunXlsxDpcData(test_cases, debug = tracer.debug)
    status = executer.start()
    for fs,caseid in status:                      
        test_result = executer(module).queue(fs)
        
        if not judgement(test_result[0], test_result[1], caseid):            
            break
        
if __name__ == "__main__":
    tracer.set_proj_path("ironpythontest", r'D:\auto\python\app-autoDebug\appDebugProject', sysencoding = False)

    t = {"a1":{'head': 5, 'casetype': u'WEB', 'description': 3, 'tester': u'sd', 'precommand': {}, 'verify': u'Result.Normal("\u524d\u7f6e\u64cd\u4f5c")', 'postcommand': {}, 'stepdescription': '', 'steps': {}, 'data': 6}}
    ttt(t,"test")
            
            