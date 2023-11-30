#decoding=gbk
from shujuku8 import suju
from pltkey import pltkey
import numpy
from methods import *
a=input('查看厂商扣1，查看标签扣2') #一切的一切都可以在这个库里进行正向或反向处理了
def shuru():
    b=input('信息:')
    return b
if a=='1':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('厂商',b))    
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
         x.append(i['厂商'])
         y.append(i['数量'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])
if a=='3':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('标签',b))
    for i in shuju:
         x.append(i['厂商'])
         y.append(i['数量'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])
