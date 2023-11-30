#decoding=gbk
from math import prod
from shujukuall import shujukuchangshi,shujukuquanbu
from itertools import product
from methods import *
from pltkey import *
from 实际排序函数 import *
def randomtuijian(biaoqian):
    a=shujukuchangshi()
    biaoqian=zhuan(biaoqian)      #这一步需要的是标签和番号的数量来求出中断的值,不求标签也可以
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
        data=list(a.chazhaoyidian('标签',i))[0]['番号']
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
    biaoqian=zhuan(biaoqian)      #这一步需要的是标签和番号的数量来求出中断的值,不求标签也可以
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
        data=list(a.chazhaoyidian('标签',i))[0]['番号']
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