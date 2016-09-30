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
import os,xmlrpclib,subprocess,re
from SimpleXMLRPCServer import SimpleXMLRPCServer
import pub
from pyrunner.executer import tracer,RunXlsxDpcData
from pyrunner.common import p_common,p_env

pub.set_path()
    
class _MyXMLRPCServer:
    def __init__(self,host = "localhost", port = 0):
        self.server = SimpleXMLRPCServer((host, port))
        self.host, self.port = self.server.socket.getsockname()
        self.server.register_introspection_functions()
        self.ENDTAG = "<RemoteTestEnd.>"
        self.__register()
        print "<RemoteTestStart:%s>" %self.port
    
    def __register(self):        
        self.server.register_function(self.__define_run_pc, 'run_pc')
        self.server.register_function(self.__define_keys, 'set_keys_module')
        self.server.register_function(self.__get_var, 'get_var')    
       
    def __get_var(self,var):
        pass
    
    def __define_keys(self, module_name):
        self.module = __import__(module_name)
        return True
        
    def __define_run_pc(self, test_cases):
        result = False
        executer    = RunXlsxDpcData(test_cases, debug = tracer.debug)
        status = executer.start()
        for fs,caseid in status:                  
            test_result = executer(self.module).queue(fs)
            
            if not pub.judgement(test_result[0], test_result[1], caseid):            
                break
            result = p_env.CASE_PASS
        print self.ENDTAG
        return result
        
def start_subprocess_server(port, subprocess_arglist=None):
    ipy_exe_str = os.popen('ipy.exe -c "import sys;print sys.executable"').read()
    
    if ipy_exe_str:
        ipypath = ipy_exe_str.strip()
    else:
        print "No ipy.exe installed"
        return
    
    if subprocess_arglist is None:
        p = r'D:\auto\python\app-autoApp'
        command = "__import__('sys').path.extend([%r,%r]);__import__('r_server')._MyXMLRPCServer(port = %d).server.serve_forever()" %(os.path.dirname(os.path.abspath(__file__)),p, port)
        subprocess_arglist = [ipypath] +  ["-c", command]          
        
    args = subprocess_arglist
    subp = subprocess.Popen(args, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    #please remember to kill subprocess -> subp.kill()
    
    return subp        

class MyXMLRPCClient:
    ''' Sample usage:
            # start server
            subp = start_subprocess_server(port = 5820)
            
            # get client 
            clt = MyXMLRPCClient(subp)
            print clt.get_rpc_methods()
            
            # send rpc request
            rpcclt = clt.get_rpc_client()
            t = {"a1":{'head': 5, 'casetype': u'WEB', 'description': 3, 'tester': u'sd', 'precommand': {}, 'verify': u'Result.Normal("\u524d\u7f6e\u64cd\u4f5c")', 'postcommand': {}, 'stepdescription': '', 'steps': {}, 'data': 6}}
            rpcclt.run_pc(t)
            
            # get output util response
            clt.poll_response(clt.subp_end_expect) 
            
            # kill
            subp.kill() 
    '''
    
    def __init__(self, subp):        
        self.subp = subp
        self.subp_start_expect = "<RemoteTestStart:(.*)>"
        self.subp_end_expect = "<RemoteTestEnd.>"
        
        port = self.poll_response(self.subp_start_expect)   
        self.client = xmlrpclib.ServerProxy('http://localhost:%s' %port)
                
    def get_rpc_client(self):
        return self.client
    
    def get_rpc_methods(self):
        return self.client.system.listMethods()
    
    def poll_response(self, expect = None):        
        subp = self.subp    
        while subp.poll()==None:
            next_line = subp.stdout.readline().decode(p_common.encoding)
            if next_line:
                print next_line
            
            if not expect:
                # will block or hang when no expect.
                continue
            
            # will block or hang when expected string not be display
            m = re.search(expect, next_line)
            if not m:
                continue
            
            if m.groups():
                return m.groups()[0]
            else:
                break 
                
        if subp.returncode:
            print "error",subp.returncode
        
def sample_usage():
    # start server
    subp = start_subprocess_server(port = 5820)
    
    # get client 
    clt = MyXMLRPCClient(subp)
    print clt.get_rpc_methods()
    
    # send rpc request
    rpcclt = clt.get_rpc_client()
    rpcclt.set_keys_module("UIPc")
    t1 = {"a1":{'head': 5, 'casetype': u'WEB', 'description': 3, 'tester': u'sd', 'precommand': {}, 'verify': u'Result.Normal("\u524d\u7f6e\u64cd\u4f5c")', 'postcommand': {}, 'stepdescription': '', 'steps': {}, 'data': 6}}
    t2 = {"a2":{'head': {}, 'casetype': u'PC', 'description': '', 'tester': '', 'precommand': {}, 'verify': u'Result.Normal("Start example test.")', 'postcommand': {}, 'stepdescription': '', 'steps': {'Step_1_info': u'WindowP.StartAppliaction(r"D:\\auto\\buffer\\AiSchool\\AiTeacherCenter\\AiTeacherCenter\\AiTeacher.exe")'}, 'data': {}}}
    t3 = {u'a5': {'head': {}, 'casetype': u'PC', 'description': '', 'tester': '', 'precommand': {}, 'verify': u'Result.Normal("Start example test.")', 'postcommand': {}, 'stepdescription': '', 'steps': {}, 'data': {}}}
    t4 = {u'a6': {'head': {}, 'casetype': u'PC', 'description': '', 'tester': '', 'precommand': {}, 'verify': u'Result.Normal("Start example test.")', 'postcommand': {}, 'stepdescription': '', 'steps': {'Step_1_info': u'LoginPC.TextUserName.TypeInWin("Hello MUIA.")'}, 'data': {}}}
    t5 = {u'a7': {'head': {}, 'casetype': u'PC', 'description': '', 'tester': '', 'precommand': {}, 'verify': u'Result.Normal("Start example test.")', 'postcommand': {}, 'stepdescription': '', 'steps': {'Step_6_info': u'LoginPC.BtnLogin.IsKeyboardFocusable()', 'Step_4_info': u'LoginPC.CkbIsSavePwd.SwitchToggle()', 'Step_3_info': u'LoginPC.CkbIsSavePwd.Name()', 'Step_7_info': u'LoginPC.BtnLogin.ClickWin() ', 'Step_1_info': u'LoginPC.PwdUser.IsPassword()', 'Step_5_info': u'LoginPC.BtnLogin.Name()', 'Step_2_info': u'LoginPC.PwdUser.TypeInWin("123456")'}, 'data': {}}}
    for case in (t1,t2,t3,t4,t5):
        rpcclt.run_pc(case)     
        # get output util response
        clt.poll_response(clt.subp_end_expect)
         
    #kill
    subp.kill()

if __name__ == "__main__":
    sample_usage() 
    


            