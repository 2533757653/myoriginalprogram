#decoding=gbk
from math import prod
from shujukuall import shujukuchangshi,shujukuquanbu
from itertools import product
from methods import *
from pltkey import *
from ʵ�������� import *
def randomtuijian(biaoqian):
    a=shujukuchangshi()
    biaoqian=zhuan(biaoqian)      #��һ����Ҫ���Ǳ�ǩ�ͷ��ŵ�����������жϵ�ֵ,�����ǩҲ����
    fina=shujukuquanbu()
    finaldata=[]
    biaoqian=findmost(biaoqian)
    shuzi=[]
    finalbiao=[]
    for i in biaoqian:
        shuzi.append(i[1])
        finalbiao.append(i[0])
    finalbiao=finalbiao[1:5]
    zuhebiao=list(product(finalbiao,finalbiao))
    for i in zuhebiao:
        data=list(a.chazhaoyidian('��ǩ',i))[0]['����']
        for q in data:
            for w,wq in zip(finaldata,range(len(finaldata))):
                if w[0]==q[0]:
                    finaldata[wq][1]=w[1]+finaldata[wq][1]
                    break
            else:
                finaldata.append(q)
    finaldata=sorted(finaldata,key=jiexi,reverse=True)
    x,y=zhuana(finaldata)
    pri12(biaoqian,x)
    #cz.zhexian(x[:30],y[:30])
def randomtui(biaoqian):
    a=shujukuchangshi()
    biaoqian=zhuan(biaoqian)      #��һ����Ҫ���Ǳ�ǩ�ͷ��ŵ�����������жϵ�ֵ,�����ǩҲ����
    fina=shujukuquanbu()
    finaldata=[]
    biaoqian=findmost(biaoqian)
    shuzi=[]
    finalbiao=[]
    for i in biaoqian:
        shuzi.append(i[1])
        finalbiao.append(i[0])
    finalbiao=finalbiao[1:5]
    zuhebiao=list(product(finalbiao,finalbiao))
    for i in zuhebiao:
        data=list(a.chazhaoyidian('��ǩ',i))[0]['����']
        for q in data:
            for w,wq in zip(finaldata,range(len(finaldata))):
                if w[0]==q[0]:
                    finaldata[wq][1]=w[1]+finaldata[wq][1]
                    break
            else:
                finaldata.append(q)
    finaldata=sorted(finaldata,key=jiexi,reverse=True)
    x,y=zhuana(finaldata)
    return x