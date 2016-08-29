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

import os
from haloudebug import sc
from pyrunner.tkui.ui import Window,Widget,ROOT,Tkconstants
from pyrunner.tkui import basic
from pyrunner.tkui.basic import MSG,FileDilog
from pyrunner.tkui.suite import Components

Window.widg = ROOT
Window.Top(sc.TITLE,geometry='95x35+270+80', resizable_x=1,resizable_y=1)


menubar = Widget.Menu(ROOT)
Window.Config(menu = menubar)
ROOT.option_add("*Menu.tearOff", 0)

class Menu:
    
    def __init__(self,master,loop=False):
        self.__main()
        self.process_ui = Process(master)
        sc.TREE = self.process_ui.tree
        sc.TEXTAREA = self.process_ui.textarea
        basic.mainloop(master, loop=loop)        
        
    def __main(self):
        self.process_ui = None        
        self.navigator_ui = None
        self.pop_ui = None
        self.menus = {}
        Components.GenerateMenu(menubar, sc.MENUS, self.menus)
        self.__set_menus_command()
        
    def __set_menus_command(self):
        node = self.menus.get(u"文件")
        Components.RegisterMenu(node, u"加载用例", self.__sel_file, "load_cases")
        node = self.menus.get(u"编辑")        
        Components.RegisterMenu(node, u"调试选中", self.__navigator, "aitest")
        Components.RegisterMenu(node, u"清除选中", self.__sel_file, "del_current")
        Components.RegisterMenu(node, u"清空列表", self.__sel_file, "del_all")
        node = self.menus.get(u"执行")        
        Components.RegisterMenu(node, u"已选的用例", self.__runner, "current")
        Components.RegisterMenu(node, u"加载的用例", self.__runner, "loaded")
        Components.RegisterMenu(node, u"配置的用例", self.__runner, "all")
        Components.RegisterMenu(node, u"停运后续用例", self.__runner, "stop")        
        node = self.menus.get(u"查看")
        Components.RegisterMenu(node, u"刷新日志", self.__show_log, "refresh")
        Components.RegisterMenu(node, u"控制台日志", self.__show_log)
        Components.RegisterMenu(node, u"测试报告", self.__show_log, "report")
        node = self.menus.get(u"帮助")
        Components.RegisterMenu(node, u"关于", self.__about)
        
    def __navigator(self,*args):
        self.__clean_ui()
        self.pop_ui = Widget.NewTop()
            
        if args[0] == "aitest":
            self.pop_ui.geometry("40x2+175+175")
            if not sc.RUNNER or not sc.INTEG:
                self.pop_ui.destroy()
                MSG.Showwarning("Waring", "No cases have been loaded.")
                return
            
            items = sc.TREE.selection()
            
            if not items:
                self.pop_ui.destroy()    
                return
#             idx = sc.TREE.index(items[0])
            
            caseid = sc.CASE_MAP.get(items[0])
            if caseid:
                self.navigator_ui = AiTest(self.pop_ui)            
                self.navigator_ui.set_testcase_to_ui(caseid)
            
    
    def __show_log(self, *args):
        self.process_ui.show(*args)
    
    def __sel_file(self,*args):
        
        if args[0] == "del_current":
            for item in sc.TREE.selection():
                sc.TREE.delete(item)
                sc.CASE_ITEMS.remove(item)
                caseid = sc.CASE_MAP.pop(item,None)
                if caseid:
                    sc.CASE_SORTED_IDS.remove(caseid)
        
        if args[0] == "del_all":
#             sd.clear_case_tree()
            MSG.Showinfo("todo", "delete all.")
        
        if args[0] == "load_cases":
#             sc.RUNNER = sd.Runner()
            MSG.Showinfo("todo", "load cases.")
            excel_path = FileDilog.Askopenfilename(filetypes = [("Excel","*.xlsx"),("Excel2003","*.xls")],initialdir = sc.AITEST_CONFIG["proj_path"])
            
            if not excel_path:
                return
            
            try:
                excel_name = os.path.basename(excel_path)                
                sc.INTEG = None
                sc.DISB = None
                sc.AITEST_CONFIG["excel_name"] = excel_name                
#                 sc.RUNNER.set_handsome(excel_name)                
#                 sd.set_case_tree()

            except Exception,e:
                MSG.Showerror("Error.", "Invalid Excel File.\n%s" %e)

    def __runner(self,*args):

        if args[0] == "all":
            sc.STOP = False
            sc.PROCESSBAR.start()
            
#             if not sc.RUNNER or sc.RUNNER.TAG:                
#                 sc.RUNNER = sd.Runner()
#             sc.RUNNER.swt = "all"
#             sc.RUNNER.setDaemon(True)
#             sc.RUNNER.start()
            MSG.Showinfo("todo", "run all cases.")                    
        elif args[0] == "stop":
            sc.STOP = True
        else:
            sc.STOP = False
#             if not sc.RUNNER or not sc.INTEG:
#                 MSG.Showwarning("Waring", "No cases have been loaded.")
#                 return
#                             
#             sc.PROCESSBAR.start()
#             
#             if sc.RUNNER.TAG:       
#                 sc.RUNNER = sd.Runner()
#                 sc.RUNNER.set_handsome(sc.AITEST_CONFIG["excel_name"])
#             
#             if args[0] == "current":
#                 sc.RUNNER.swt = "current"
#                 
#             if args[0] == "loaded":
#                 sc.RUNNER.swt = "loaded" 
#                 
#             sc.RUNNER.setDaemon(True)
#             sc.RUNNER.start()
            MSG.Showinfo("todo", "run testcases in configuration.")
        
            
    def __about(self):
        version = "1.0.0"
        date = "20160829"
        MSG.Showinfo(u'Version: Twsm Release (%s)' %version, 
                     'Version:\t%s\nCurrent Update:\t%s\n\nAuthor:\t\t罗科峰(Bruce Luo)\nBuild from:\t20160829\nMail:\t\tlkf20031988@163.com\n\n\t(c)Copyright tools contributors and others\n' %(version,date))
    
    def __clean_var(self):
        sc.RUNNER = None
        sc.INTEG = None
        sc.DISB = None
        sc.CASE_ITEMS = []
        
    def __clean_ui(self):
        if self.navigator_ui:
            self.navigator_ui.destroy()
            self.navigator_ui = None

class AiTest:
    
    def __init__(self,master = ROOT, loop = False):
        self.__master = master
        self.__main()        
        basic.mainloop(master, loop=loop)
    
    def __main(self):
        self.frame1             = Widget.Labelframe(self.__master)
        self.frm_steps          = Widget.Labelframe(self.frame1)        
        self.frm_precommand     = Widget.Labelframe(self.frame1)
        self.frm_head           = Widget.Labelframe(self.frame1)
        self.frm_data           = Widget.Labelframe(self.frame1)
        self.frm_postcommand    = Widget.Labelframe(self.frame1)
        self.frm_verify         = Widget.Labelframe(self.frame1)        
        self.frm_basic_info     = Widget.Labelframe(self.__master)
        self.frm_confirm        = Widget.Labelframe(self.__master)
        self.frm_formator       = Widget.Labelframe(self.__master)
        
        # frame1     
        Window.widg = self.frame1
        Window.Config(text = "Case")
        Window.Pack(side = "top", fill = Tkconstants.BOTH, expand = Tkconstants.YES,padx = "0.2c")
        
        text_conf={"font":"Calibri 10", "width" : 40, "height": 2, "wrap" :"none"}
        for i in ["steps","precommand","head","data","postcommand","verify"]:
            sc.CASE[i] = Components.TextWithScrollbar(getattr(self, "frm_%s" %i))[0]
            
            Window.widg = sc.CASE[i]
            Window.Config(**text_conf)
            
            Window.widg = getattr(self,"frm_%s" %i)
            Window.Config(text = i.capitalize())
            if i in ["steps","postcommand", "verify"]:
                side = "left"
            else:
                side = "top"
                
            Window.Pack(side = side, fill = Tkconstants.BOTH, expand = Tkconstants.YES)
        
        # frame2
        Window.widg = self.frm_basic_info
        Window.Config(text = "Basic Info.")
        Window.Pack(side="left",fill = Tkconstants.X)
        
        grid_tree = [
                        [("TestCaseID:","")],
                        [("Description:","")],
                        [("CaseType:","")],
                        [("Tester:","")],                        
                     ]
        
        widgets = Components.LabelWithEntryAndButton(self.frm_basic_info, grid_tree)
        entry_caseid    = widgets[0][1]
        entry_descript  = widgets[1][1]
        entry_casetype  = widgets[2][1]
        entry_tester    = widgets[3][1]
        
        entry_conf = {"width":50}
        Window.widg = entry_caseid
        Window.Config(state = "disabled")
        Window.Config(**entry_conf)
        sc.CASE["caseid"] = Window.ConfigVar("textvariable")        
        
        Window.widg = entry_descript
        Window.Config(**entry_conf)
        sc.CASE["description"] = Window.ConfigVar("textvariable")
                       
        Window.widg = entry_casetype
        Window.Config(**entry_conf)
        sc.CASE["casetype"] = Window.ConfigVar("textvariable")
                 
        Window.widg = entry_tester
        Window.Config(**entry_conf)
        sc.CASE["tester"] = Window.ConfigVar("textvariable")
        
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
                
        # bind
        Window.widg = self.__master
        Window.Bind("<Control-Key-a>", self.__select_all_text, className = "Text")
        Window.Bind("<Control-Key-A>", self.__select_all_text, className = "Text")
                
    def confirm(self):
#         if not sc.RUNNER or not sc.INTEG:            
#             MSG.Showwarning("Waring", "No cases have been loaded.")                       
#             return
            
#         tmp_case = sd.set_case_value()        
#         if not tmp_case:
#             return        
#         sc.INTEG.testSet.update(tmp_case)
        MSG.Showinfo("todo", "confirm data.")
        self.destroy()
         
    
    def set_testcase_to_ui(self,caseid):
#         case = sc.INTEG.testSet.get(caseid)
#         
#         raw_case = sd.unset_case_value(case)
#         
#         sc.CASE["caseid"].set(caseid)
#         sc.CASE["description"].set(raw_case.get("description"))
#         sc.CASE["casetype"].set(raw_case.get("casetype"))
#         sc.CASE["tester"].set(raw_case.get("tester"))        
#         
#         for i in ["steps","precommand","head","data","postcommand","verify",]:
#             sc.CASE[i].delete("1.0","end")        
#             sc.CASE[i].insert("end",raw_case.get(i))
#             sc.CASE[i].see("end")
#             sc.CASE[i].update()
        MSG.Showinfo("todo", "show cases data to ui.")
    def __select_all_text(self,event):
        text = event.widget
        text.tag_add(Tkconstants.SEL, "1.0", Tkconstants.END)
    
    def __ui_format(self,formt = True):
#         for i in ["steps","precommand","head","data","postcommand","verify"]:
#             strs = sc.CASE[i].get("1.0","end").strip()
#             
#             if formt == "seqfy":                
#                 seq_str = sd.setCaseSteps(strs, seqfy=True)
#             elif formt == "unseqfy":
#                 seq_str = sd.unSetCaseSteps(strs, unseqfy=True)
#             else:
#                 continue
#                 
#             sc.CASE[i].delete("1.0","end")
#             sc.CASE[i].insert("end",seq_str)
        MSG.Showinfo("todo", "format ui data.")
        
    def destroy(self):
        self.__master.destroy()
        sc.CASE = {"caseid":None,
            "casetype":None,
            "tester":None,
            "steps":None,
            "description":None,
            "precommand":None,
            "head":None,
            "data":None,
            "postcommand":None,
            "verify":None,
            }
        
class Process:
    ''' Process(ROOT, loop = True) '''
    
    def __init__(self,master = ROOT,loop = False):
        self.__master = master
        self.__main()
        basic.mainloop(master, loop=loop)
        
    def __main(self):
        (self.__pane, frame1, self.__frame2) = Components.PaneWithLabelframe(self.__master, "TestCases", "Console", orient= Tkconstants.HORIZONTAL)
        frame3 = Widget.Labelframe(self.__master)
        sc.PROCESSBAR          = Widget.Progressbar(frame3)
        
        # frame3 
        Window.widg = frame3
        Window.Config(text = "Process")
        Window.Pack(side = "bottom", fill = Tkconstants.BOTH, expand = Tkconstants.NO,padx = "0.2c")
        
        Window.widg = sc.PROCESSBAR  
        Window.Pack(side="top", fill = Tkconstants.BOTH, expand = Tkconstants.YES,padx = "0.2c")
        
        # frame1
        self.tree = Components.TreeviewWithScrollbar(frame1, ["NO.","TestCase","Status"])[0]
        self.tree.column("col0", width = 10)
        self.tree.tag_configure('tag_black',foreground = 'black')
        self.tree.tag_configure('tag_yellow',foreground = 'yellow')
        self.tree.tag_configure('tag_red',foreground = 'red')
        Window.widg = self.tree
        Window.Bind("<Double-Button-1>", self.__open_case_detail_ui)   
        Window.Pack(side = "top", fill="both", expand="yes", pady=2, padx=2)
        
        # frame2
        text_conf={"font":"Calibri 10", "width" : 75, "height": 15, "wrap" :"none"}
        self.textarea = Components.TextWithScrollbar(self.__frame2)[0]
        Window.widg = self.textarea
        Window.Config(**text_conf)
        Window.Pack(side = "top", fill="both", expand="yes", pady=2, padx=2)
        self.__pane.forget(self.__frame2) 
        
        # bind
        Window.widg = self.textarea
        Window.Bind("<Key-F5>", self.show, "refresh")
        
    
    def show(self, *args):
        if not args:
            self.__show_console()            
            
        elif args[0] == "report":
#             sd.view_report()
            MSG.Showinfo("todo", "show report in browser.")
            return
        
        if sc.RUNNER and os.path.exists(sc.AITEST_CONFIG["log_file"]):
            with open(sc.AITEST_CONFIG["log_file"], "r") as f:
                self.textarea.delete("1.0","end")
                self.textarea.insert("end", f.read())
#             self.textarea.see("end")
            self.textarea.yview_moveto(1)
                
    def __show_console(self):
        if basic.get_widget_ismapped(self.__frame2):
            self.__pane.forget(self.__frame2)
        else:
            self.__pane.add(self.__frame2)
     
    
    def __open_case_detail_ui(self, event):
        self.pop_ui = Widget.NewTop()            
        
        items = self.tree.selection()
        if not items:
            self.pop_ui.destroy()  
            MSG.Showwarning("Waring", "No items has been selected.")              
            return
        
#         caseid = sc.CASE_MAP.get(items[0])
#         if caseid:
#             self.navigator_ui = AiTest(self.pop_ui)            
#             self.navigator_ui.set_testcase_to_ui(caseid)
            
    def destroy(self):
        self.__pane.destroy()



if __name__ == "__main__":
#     Menu(ROOT, loop = True)
#     AiTest(ROOT, loop = True)
    Process(ROOT, loop = True)
    