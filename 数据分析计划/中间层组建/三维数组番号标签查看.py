#decoding=gbk
from shujuku6 import suju
from pltkey import pltkey
from methods import *
import numpy
a=input('查看番号扣1，查看标签扣2')
def shuru():
    b=input('信息:')
    return b
if a=='1':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('番号',b))
    for i in shuju:
         x.append(i['标签'])
         y.append(i['数量'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])
if a=='2':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('标签',b))
    for i in shuju:
         x.append(i['番号'])
         y.append(i['数量'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])