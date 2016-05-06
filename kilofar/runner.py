# -*- encoding: utf-8 -*-
'''
Current module: kilofar.runner

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      kilofar.runner,v 1.0 2016年5月6日
    FROM:   2016年5月6日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from pyrunner.executer import RunModule
from pyrunner.common import p_common


def run_testcases(section,module_name={},case_name = None,):  
    p_common.config = p_common.get_current_config(section)
    
    executer    = RunModule(module_name)
    status      = executer.start()
     
    for rs,case_name in status:
        executer.judgement(rs)
        
        
