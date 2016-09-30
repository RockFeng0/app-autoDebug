# -*- encoding: utf-8 -*-
'''
Current module: uiexe

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      uiexe,v 1.0 2016年8月29日
    FROM:   2016年8月29日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import sys,os,time,webbrowser

import sc,r_server
from pyrunner.tkui.ui import Window,Widget,ROOT,Tkconstants
from pyrunner.tkui import basic
from pyrunner.tkui.basic import MSG,FileDilog
from pyrunner.tkui.suite import Components
from pyrunner.ext.idleshell.TextEditDelegator import TextEditDelegator
from pyrunner.ext.idleshell.SimpleAutoComplete import SimpleAutoComplete
from pyrunner.ext.idleshell.diyrpc import TkConsole,MyInterp,MyRpcClient
from pyrunner.common import p_common,p_env

Window.widg = ROOT
Window.Top(sc.TITLE,geometry='95x35+270+80', resizable_x=1,resizable_y=1)

menubar = Widget.Menu(ROOT)
Window.Config(menu = menubar)
ROOT.option_add("*Menu.tearOff", 0)
        
class AiTest:
    
    def __init__(self,master = ROOT, feature = {}, basic_field = [], rpcclt = None, loop = False):
        self.__master = master
        self.__feature = feature
        self.__basic_field = basic_field
        self.__rpcclt = rpcclt
        
        self.__radio_texts = []
        if feature:
            self.__radio_texts = feature.get("info")
            self.__radio_texts = self.__radio_texts + feature.get("step")
            self.__radio_texts.append(feature.get("unique"))
        
            if basic_field:
                self.__radio_texts = list(set(self.__radio_texts) - set(basic_field))
        
        self.__main()
        basic.mainloop(master, loop=loop)
    
    def __main(self):
        self.frm_swt        = Widget.Labelframe(self.__master)
        self.frm_basic      = Widget.Labelframe(self.__master)
        self.frm_field      = Widget.Labelframe(self.__master)
        self.frm_formator   = Widget.Labelframe(self.__master)
        self.frm_confirm    = Widget.Labelframe(self.__master)

        # Switcher frame
        Window.widg = self.frm_swt
        Window.Config(text = "Switcher")
        Window.Pack(side = "left", fill="both", expand="no", padx = "0.2c")        
        self.radio_var = Components.RadioWithLabelframe(self.frm_swt,
                                                        texts = self.__radio_texts,
                                                        values = self.__radio_texts,
                                                        command = self.set_field_value2edit)[0]
        
        # Basic frame
        Window.widg = self.frm_basic
        Window.Config(text = "Basic Info.")
        Window.Pack(side="top",fill = Tkconstants.X)
        
        grid_tree = []
        for f in self.__basic_field:
            grid_tree.append([("%s:" %f,"")])
#         print grid_tree        
        widgets = Components.LabelWithEntryAndButton(self.frm_basic, grid_tree)
        entry_caseid    = widgets[0][1]
        entry_descript  = widgets[1][1]
        entry_casetype  = widgets[2][1]
        entry_tester    = widgets[3][1]
        
        entry_conf = {"width":50}
        Window.widg = entry_caseid
        entry_caseid.insert("end",sc.CASE["id"])
        Window.Config(state = "disabled")
        Window.Config(**entry_conf)        
        
        Window.widg = entry_descript
        Window.Config(**entry_conf)
        v = sc.CASE["value"].get("description")
        if v:
            entry_descript.insert("end",p_common.unstepfy(v))
        Window.Config(state = "disabled")
                       
        Window.widg = entry_casetype
        Window.Config(**entry_conf)
        v = sc.CASE["value"].get("casetype")
        if v:
            entry_casetype.insert("end",p_common.unstepfy(v))
        Window.Config(state = "disabled")
        
        Window.widg = entry_tester
        Window.Config(**entry_conf)
        v = sc.CASE["value"].get("tester")
        if v:
            entry_tester.insert("end",p_common.unstepfy(v))
        Window.Config(state = "disabled")
        
        # Field frame
        Window.widg = self.frm_field
        Window.Pack(side = "top", fill="both", expand="yes", padx = "0.2c")
        
        self.edit_text = Components.TextWithScrollbar(self.frm_field)[0]
        ted = TextEditDelegator(self.edit_text)    
        ted.effect_on_text("STRING", {'font': u"Calibri 10",'foreground': 'red','background': '#ffffff'})
        
        sac = SimpleAutoComplete(self.edit_text, rpcclt=self.__rpcclt)
        self.edit_text.bind('<Alt-Key-/>', sac.autocomplete_event)    
                
        text_conf={"font":"Calibri 10", "width" : 40, "height": 2, "wrap" :"none"}
        Window.widg = self.edit_text
        Window.Config(**text_conf)                

        # Formator frame
        Window.widg = self.frm_formator
        Window.Config(text = "Formator.")
        Window.Pack(side="top",fill = Tkconstants.X)
         
        button1 = Widget.Button(self.frm_formator)
        button2 = Widget.Button(self.frm_formator)
                 
        Window.widg = button1
        cmd1 = basic.register_command(button1, self.__ui_format, "seqfy")    
        Window.Config(text = u"序列化", command = cmd1)
        Window.Pack(side = "left",padx = "50")
         
        Window.widg = button2
        cmd2 = basic.register_command(button1, self.__ui_format, "unseqfy")
        Window.Config(text = u"反序列化", command = cmd2)
        Window.Pack(side = "left",padx = "50")        
         
        # Confirm frame
        Window.widg = self.frm_confirm
        Window.Config(text = "Confirm.")
        Window.Pack(side="bottom",fill = Tkconstants.X)
         
        button3 = Widget.Button(self.frm_confirm)
        button4 = Widget.Button(self.frm_confirm)
                 
        Window.widg = button3
        Window.Config(text = u"提交", command = self.confirm)
        Window.Pack(side = "left",padx = "50")
         
        Window.widg = button4
        Window.Config(text = u"取消", command = self.destroy)
        Window.Pack(side = "left",padx = "50")
    
    def set_field_value2edit(self):
        if self.frm_field:
            self.frm_field.config(text = self.radio_var.get())
            self.edit_text.delete("1.0","end")
            if sc.CASE["id"]:
                k = self.radio_var.get().lower()
                v = sc.CASE["value"].get(k)
                self.edit_text.insert("end",p_common.unstepfy(v))
            else:
                self.edit_text.insert("end",self.radio_var.get())
                     
    def confirm(self):
        if not sc.CASE["id"]:
            return
        
        k = self.radio_var.get()
        v = self.edit_text.get("1.0", "end")
        if k in self.__feature["step"]:  
            if not MSG.Askyesno("", "您确认，要更新步骤[%s]吗？" %k):
                return          
            sc.CASE["value"][k.lower()] = p_common.stepfy(v)
        elif k in self.__feature["info"]:
            if not MSG.Askyesno("", "您确认，要更新[%s]吗？" %k):
                return          
            sc.CASE["value"][k.lower()] = v  
        
        if self.__rpcclt:
            self.__rpcclt.remotequeue("exec", "runcode", ('a.testSet["%s"].update(%r)' %(sc.CASE["id"],sc.CASE["value"]),), {})
        
        if MSG.Askyesno("'%s'已更新成功." %k, "是否继续修改其他项？" ):
            return
        self.destroy()
        ROOT.deiconify()                 
                 
    def __ui_format(self,formt):
        strs = self.edit_text.get("1.0","end").strip()
        if not strs:
            return
                
        if formt == "seqfy":
            strs = p_common.seqfy(strs)                
                    
        if formt == "unseqfy":
            strs = p_common.unseqfy(strs)
        
        self.edit_text.delete("1.0","end")
        self.edit_text.insert("end",strs)
       
    def destroy(self):
        ROOT.deiconify()
        self.__master.destroy()
        
class Process:
    ''' Process(ROOT, loop = True) '''
    
    def __init__(self,master = ROOT,loop = False):
        self.__master = master
        self.__main()
        basic.mainloop(master, loop=loop)
        
    def __main(self):
        ### Menu
        self.menus = {}
        Components.GenerateMenu(menubar, sc.MENUS, self.menus)
        
        ### Pane Window
        (self.__pane, frame1, self.__frame2) = Components.PaneWithLabelframe(self.__master, "TestCases", "Console", orient= Tkconstants.HORIZONTAL)
        frame3 = Widget.Labelframe(self.__master)
        self.processbar          = Widget.Progressbar(frame3)
        
        # frame3 
        Window.widg = frame3
        Window.Config(text = "Process")
        Window.Pack(side = "bottom", fill = Tkconstants.BOTH, expand = Tkconstants.NO,padx = "0.2c")
        
        Window.widg = self.processbar
        Window.Pack(side="top", fill = Tkconstants.BOTH, expand = Tkconstants.YES,padx = "0.2c")
        
        # frame1
        self.tree = Components.TreeviewWithScrollbar(frame1, ["NO.","TestCase","Status"])[0]
        self.tree.column("col0", width = 10)
        self.tree.tag_configure('tag_black',foreground = 'black')
        self.tree.tag_configure('tag_yellow',foreground = '#FFA500')
        self.tree.tag_configure('tag_red',foreground = 'red')
                
        # frame2
        text_conf={"font":"Calibri 10", "width" : 75, "height": 15, "wrap" :"none"}
        self.textarea = Components.TextWithScrollbar(self.__frame2)[0]
        Window.widg = self.textarea
        Window.Config(**text_conf)
        Window.Pack(side = "top", fill="both", expand="yes", pady=2, padx=2)
        self.__pane.forget(self.__frame2)                 
                    
    def show_console(self):
        if basic.get_widget_ismapped(self.__frame2):
            self.__pane.forget(self.__frame2)
        else:
            self.__pane.add(self.__frame2)
    
    def destroy(self):
        self.__pane.destroy()

class PyConsole:
    
    def __init__(self, master = ROOT, loop = False):
        self.api_path = os.path.abspath(sys.path[0]).decode("cp936")        
        proj_path = os.path.join(self.api_path, sc.PROJ_NAME)
        
        p_common.init_project_env(sc.PROJ_NAME, proj_path= proj_path)
        self.__proj_config = p_common.get_current_config("PROJECTCONFIG")
         
        self.__master = master
        self.process_ui = Process(master)
        self.__set_menus_command(self.process_ui.menus)        
        self.__init_rpc(self.process_ui.textarea)       
                 
        self.__main()
        basic.mainloop(master, loop=loop)        
    
    def __init_rpc(self, tktext):
        
        # tkconsole             
        tkconsole = TkConsole(tktext)
        
        # interpreter
        api_file_path = os.path.join(self.api_path,"%s.py" %sc.KEYS_MODULE_NAME.get("web"))
        self.intp = MyInterp(tkconsole)
        self.intp.start_subprocess(api_file_path)
        self.intp.extend_namespace(api_file_path)
        self.intp.runsource("from sd import SdRunner;a = SdRunner('%s',debug = True)" %(self.__proj_config.get("config")))
        
        # rpc client
        self.clt = MyRpcClient(self.intp.rpcclt)
        
        # text delegator
        ted = TextEditDelegator(tktext)        
        ted.effect_on_text('ERROR', {'foreground': '#000000','background': '#ff7777'})
        
        # start ironpython rpc server
#         self.intp.runsource("import r_server;ipy_subp = r_server.start_subprocess_server(port = 0)")
#         self.intp.runsource("ipy_clt = r_server.MyXMLRPCClient(ipy_subp);ipy_rpcclt = ipy_clt.get_rpc_client();ipy_rpcclt.set_keys_module('%s')" %(sc.KEYS_MODULE_NAME.get("pc")))
        
        self.intp.runsource("""
import r_server
ipy_subp = r_server.start_subprocess_server(port = 0)
ipy_subp_tag = False
if ipy_subp:
    ipy_clt = r_server.MyXMLRPCClient(ipy_subp)
    ipy_rpcclt = ipy_clt.get_rpc_client()
    ipy_rpcclt.set_keys_module('%s')
    ipy_subp_tag = True
""" %(sc.KEYS_MODULE_NAME.get("pc")), symbol = "exec")
                           
        
    def __set_menus_command(self, menus_map):
        node = menus_map.get(u"文件")
        Components.RegisterMenu(node, u"加载用例", self.__sel_file, "load_cases")
        node = menus_map.get(u"编辑")
        Components.RegisterMenu(node, u"清除选中", self.__sel_file, "del_current")
        Components.RegisterMenu(node, u"清空列表", self.__sel_file, "del_all")
        node = menus_map.get(u"执行")    
        Components.RegisterMenu(node, u"已选的用例", self.__runner, "current")
        Components.RegisterMenu(node, u"加载的用例", self.__runner, "loaded")
        Components.RegisterMenu(node, u"配置的用例", self.__runner, "all")
        Components.RegisterMenu(node, u"停运后续用例", self.__runner, "stop")        
        node = menus_map.get(u"查看")        
        Components.RegisterMenu(node, u"控制台日志", self.__show_console)
        Components.RegisterMenu(node, u"测试报告", self.__show_report)
        node = menus_map.get(u"帮助")
        Components.RegisterMenu(node, u"关于", self.__about)
        
    def __main(self):
        self.feature = []
        self.testSet = {}
        self.__tree_items = []
        self.__sorted_cases_id = []
        self.__item_map_case = []
        self.__running_stop = False
        
        Window.widg = self.process_ui.tree
        Window.Bind("<Double-Button-1>", self.__open_case_detail_ui)   
        Window.Pack(side = "top", fill="both", expand="yes", pady=2, padx=2)
        
        
    def __sel_file(self,*args, **kwargs):
        
        if args[0] == "load_cases":
            excel_name = kwargs.get("excel_name")
            if not excel_name:
                excel_path = FileDilog.Askopenfilename(filetypes = [("Excel","*.xlsx"),("Excel2003","*.xls")],initialdir = None)
                if not excel_path:
                    return
                excel_name = os.path.basename(excel_path)            
            try:
                excel_info_fields = ["TestCaseID","Description","Verify","StepDescription","Tester", "CaseType"]
                self.intp.runsource('a.set_feature("%s",info=%r)' %(excel_name, excel_info_fields))
                self.feature = self.clt.remotequeue("exec", "poll_var", ('a',"testFeature"), {})
                self.testSet = self.clt.remotequeue("exec", "poll_var", ('a',"testSet"), {})                
                self.__set_case_tree()             
            except Exception,e:
                MSG.Showerror("Error.", "Invalid Excel File.\n%s" %e)
                
        if args[0] == "del_current":
            for item in self.process_ui.tree.selection():
                self.process_ui.tree.delete(item)
                self.__tree_items.remove(item)
                caseid = self.__item_map_case.pop(item,None)
                if caseid:
                    self.__sorted_cases_id.remove(caseid)
        
        if args[0] == "del_all":
            self.__clear_case_tree()
    
    def __clear_case_tree(self):
        for item in self.__tree_items:
            self.process_ui.tree.delete(item)
        self.__tree_items = []
        self.__sorted_cases_id = []
        self.__item_map_case = []
        
    
    def __generate_cases2tree_value(self):
        result =[]
        if not self.testSet:
            return result
        
        caseids = self.testSet.keys()        
        
        if caseids:
            j = 0
            self.__sorted_cases_id = p_common.get_sorted_list(caseids)
            for i in self.__sorted_cases_id:
                twsm_case = self.testSet[i]
                case_name = p_common.get_legal_filename("%s[%s]" %(i,unicode(twsm_case["description"])))
                result.append((j, case_name, "Ready"))
                j = j + 1
        
        return result
        
    def __set_case_tree(self):
        self.__clear_case_tree()
        self.__tree_items = []
        datas = self.__generate_cases2tree_value()                
        for data in datas:                
            self.__tree_items.append(self.process_ui.tree.insert("","end", values = data))
            self.process_ui.tree.update()
            
        self.__item_map_case = dict(zip(self.__tree_items, self.__sorted_cases_id))
        
    def __runner(self,*args):

        if args[0] == "all":
            self.process_ui.processbar.start()
            excels = self.__proj_config.get("excel_cases").split(";")
            tmp = []
            for i in excels:
                if not os.path.isfile(os.path.join(p_env.CASE_PKG_PATH, i)):
                    tmp.append(i)                                        
                    continue
            if tmp:
                MSG.Showwarning("Warning", "Excel casees not exist:\n%r" %tmp)
            else:
                for i in excels:
                    self.__sel_file("load_cases", excel_name = i)
                    self.__run_tree_items(self.__tree_items)
                        
            self.process_ui.processbar.stop()
                                         
        elif args[0] == "stop":
            self.__running_stop = True
            MSG.Showinfo("Stopping", "Will stop the running at next testcase.")
            self.process_ui.processbar.stop()
            
        elif args[0] == "loaded":
            self.process_ui.processbar.start()
            self.__run_tree_items(self.__tree_items)                
            self.process_ui.processbar.stop()
                            
        elif args[0] == "current":
            self.process_ui.processbar.start()            
            self.__run_tree_items(self.process_ui.tree.selection())
            self.process_ui.processbar.stop()
                        
    def __run_tree_items(self, treeitems):
                
        f_get = lambda:self.clt.remotecall("exec", "poll_var", ('a',"itemrst"), {})
        f_set = lambda:self.clt.remotecall("exec", "runcode", ('a.itemrst=None',), {})
        tested = False
        for item in treeitems:
            if self.__running_stop:
                self.__running_stop = False
                MSG.Showinfo("Running Stopped", "Stopped at testcase: %s" %self.process_ui.tree.set(item,"col1"))
                break
            self.process_ui.tree.see(item)
            self.process_ui.tree.item(item, tags = "tag_yellow")
            self.process_ui.tree.set(item, "col2", "Runing")                
            item_caseid = self.__item_map_case.get(item)
            
            case_type = self.testSet.get(item_caseid).get("casetype").lower()
            if case_type == "pc":
                result = False
                ipy_subp_tag = self.clt.remotequeue("exec", "poll_var", ("ipy_subp_tag",), {})
                if ipy_subp_tag:        
                    case = self.testSet.get(item_caseid)
                    
                    self.intp.runsource("ipy_result = ipy_rpcclt.run_pc(%r);ipy_clt.poll_response(ipy_clt.subp_end_expect)" %{item_caseid:case})
                    while True:
                        result = self.clt.remotecall("exec", "poll_var", ('ipy_result',), {})
                        if isinstance(result, bool):
                            self.clt.remotecall("exec", "runcode", ('ipy_result = None',), {})
                            break
                        self.__update_tree(0.1)
                else:
                    self.intp.runsource("Warning: ipy.exe rpc server not started.")
                self.__change_item_color_and_value(item, result)
                
            elif case_type == "web":
                self.intp.runsource('a.start_run("%s","%s")' %(sc.KEYS_MODULE_NAME.get("web"), item_caseid))        
            
                while True:
                    rst = f_get()                                           
                    if not rst:
                        tested = False
                        self.__update_tree(0.05)
                        continue
                    
                    caseid,result = rst           
                    if caseid == item_caseid:
                        tested = False                              
                    elif caseid == None and tested ==False:
                        tested = True
                        self.__change_item_color_and_value(item, result)
                        f_set()             
                        break
                    else:
                        pass
                    self.__update_tree(0.1)
    
    def __change_item_color_and_value(self, item, result):
        if result:
            val = "Pass"
            self.process_ui.tree.item(item, tags = "tag_black")                        
        else:
            val = "Fail"
            self.process_ui.tree.item(item, tags = "tag_red")                        
        self.process_ui.tree.set(item, "col2", val)
    
    def __open_case_detail_ui(self, event):
        self.pop_ui = Widget.NewTop()
        Window.widg = self.pop_ui      
        Window.Top("步骤编辑器",geometry='45x23+270+80', resizable_x=1,resizable_y=1)
        
        items = self.process_ui.tree.selection()
        if not items:
            self.pop_ui.destroy()
            MSG.Showwarning("Waring", "No items has been selected.")
            return
        
        caseid = self.__item_map_case.get(items[0])
        if caseid:            
            sc.CASE["id"] = caseid
            sc.CASE["value"] = self.testSet.get(caseid)
            basic_field = ['TestCaseID','Description','CaseType','Tester']
            self.navigator_ui = AiTest(self.pop_ui, feature = self.feature, basic_field = basic_field, rpcclt= self.clt)
            self.__master.withdraw()
    
    def __update_tree(self, wait=0.05):
        time.sleep(wait)
        self.process_ui.tree.update()
    
    def __show_console(self):
        self.process_ui.show_console()
    
    def __show_report(self):
        webbrowser.open(os.path.join(p_env.RST_PATH,"result.html"))
                
    def __about(self):
        version = "1.0.0"
        date = "20160918"
        MSG.Showinfo(u'Version: Twsm Release (%s)' %version, 
                     'Version:\t%s\nCurrent Update:\t%s\n\nAuthor:\t\t罗科峰(Bruce Luo)\nBuild from:\t20160829\nMail:\t\tlkf20031988@163.com\n\n\t(c)Copyright tools contributors and others\n' %(version,date))
                            

if __name__ == "__main__":
### main UI
#     Process(ROOT, loop = True)

### Edit UI
#     feature = {'info': ['TestCaseID', 'Description', 'Verify', 'StepDescription', 'Tester'], 'step': ['Steps', 'PreCommand', 'Head', 'Data', 'PostCommand'], 'unique': 'TestCaseID', 'sheet': 'TestCase'}
#     basic_field = ['TestCaseID', 'Description', 'CaseType', 'Tester']
#     sc.CASE={"id":"debug1","value": {}}
#     ROOT.geometry('45x23+270+80')
#     AiTest(ROOT, feature=feature, basic_field=basic_field, loop = True)

### preference main
    PyConsole(ROOT, loop = True)
    