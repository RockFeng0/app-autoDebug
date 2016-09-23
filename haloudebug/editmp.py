# -*- encoding: utf-8 -*-
'''
Current module: haloudebug.editmp

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      haloudebug.editmp,v 1.0 2016年9月1日
    FROM:   2016年9月1日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from pyrunner.ext.idleshell.TextEditDelegator import TextEditDelegator
from pyrunner.ext.idleshell.SimpleAutoComplete import SimpleAutoComplete
from pyrunner.ext.idleshell.diyrpc import TkConsole,MyInterp
from pyrunner.tkui.suite import Components
from pyrunner.tkui.ui import ROOT,Widget,Window

#### Components Text
frame1 = Widget.Labelframe(ROOT,text = "XXXX")
Window.widg = frame1        
Window.Pack(side = "top", fill="both", expand="yes", padx = "0.2c")
   
(t,x,y) = Components.TextWithScrollbar(frame1)
t.config(wrap = "none")

####  RPC and Interpreter
api_file_path = r"UIWeb.py"; # UIPc.py  ;  UIPad.py
tkconsole = TkConsole(t)
intp = MyInterp(tkconsole)
intp.start_subprocess(api_file_path)
intp.extend_namespace(api_file_path)
  
#### Text Edit
ted = TextEditDelegator(t)    
ted.effect_on_text("STRING", {'font': u"Calibri 10 normal roman",'foreground': 'red','background': '#ffffff'})

#### Text Auto Complete
sac = SimpleAutoComplete(master = t, rpcclt=intp.rpcclt, debug = False)
t.bind('<Alt-Key-/>', sac.autocomplete_event)

#### others
bt = Widget.Button(ROOT)
Window.widg = bt
def sss():        
    intp.runsource('from sd import SdRunner;a = SdRunner("env241", "tt.xlsx", debug = True);a.start_run("web")')
  
Window.Config(text = "run", command = sss)
bt.pack()

t.insert("end","0.ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss\n")
t.insert("end","1.sdf\n")
  
ROOT.mainloop()