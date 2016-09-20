# -*- encoding: utf-8 -*-
'''
Current module: testcase.ttt

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      testcase.ttt,v 1.0 2016年5月16日
    FROM:   2016年5月16日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from halou.myxml import getObjFromXmlMap

def test1():
    print u"XML object map relation:"
    getObjFromXmlMap(["Login","LoginAccountInput"]).Hello()
    return ('asdfasdf', False,u"哈哈哈")

