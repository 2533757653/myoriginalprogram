#decoding=gbk
from shujuku8 import suju
from pltkey import pltkey
import numpy
from methods import *
a=input('�鿴���̿�1���鿴��ǩ��2') #һ�е�һ�ж����������������������������
def shuru():
    b=input('��Ϣ:')
    return b
if a=='1':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('����',b))    
    for i in shuju:
         x.append(i['��ǩ'])
         y.append(i['����'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])
if a=='2':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('��ǩ',b))
    for i in shuju:
         x.append(i['����'])
         y.append(i['����'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])
if a=='3':
    b=shuru()
    c=suju()
    x=[]
    y=[]
    shuju=list(c.chazhaore('��ǩ',b))
    for i in shuju:
         x.append(i['����'])
         y.append(i['����'])
    cz=pltkey()
    x,y=sortsanwei(x,y)
    cz.zhexian(x[0:20],y[0:20])
