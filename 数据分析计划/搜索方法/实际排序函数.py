#decoding=gbk
from shujukuall import shujukuchangshi,shujukuquanbu,shujukujingjianquanbu
from methods import *
from pltkey import *
def jiexi1(a):
    return a['权重']*100
def pri(biao,shuju):
    #先将favourite内的东西取出,list1数据是往往是选出的数据，进行保存，按先后，再按，权重比进行排序，权重比按厂商和类别的概率进行排序，优先权重最高的作品。
    #排序排的很粗糙啊,排序种或许厂商会有意义
    list1=[]
    a=shujukuquanbu()
    for i in shuju[:10]:
        tem=list(a.chazhaore('番号',i))
        for q in tem:
            list1.append(q)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['标签']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['权重']=quan            #这个可以随时更改的，不用担心
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1:
        print(i['番号']+','+i['名字'])



def pri12(biao,shuju,number):
    #先将favourite内的东西取出,list1数据是往往是选出的数据，进行保存，按先后，再按，权重比进行排序，权重比按厂商和类别的概率进行排序，优先权重最高的作品。
    list1=[]
    a=shujukujingjianquanbu()
    for i in shuju[:10]:
        tem=list(a.chazhaore('_id',i))
        for q in tem:
            list1.append(q)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['标签']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['权重']=quan            #这个可以随时更改的，不用担心
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1[:number]:
        print(i['_id']+','+i['名字'])

def prileishiyong(biao,shuju,number):
    #先将favourite内的东西取出,list1数据是往往是选出的数据，进行保存，按先后，再按，权重比进行排序，权重比按厂商和类别的概率进行排序，优先权重最高的作品。
    list1=[]
    a=shujukujingjianquanbu()
    biao=zhuan(biao)      
    biao=findmost(biao)
    biao=quanzhong(biao)
    for i in shuju[:10]:
        tem=list(a.chazhaore('_id',i))
        for q in tem:
            list1.append(q)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['标签']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['权重']=quan            #这个可以随时更改的，不用担心
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1[:number]:
        print(i['_id']+','+i['名字'])

def priyiban(biao,shuju,number):
    list1=shuju
    biao=zhuan(biao)      
    biao=findmost(biao)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['标签']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['权重']=quan            #这个可以随时更改的，不用担心
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1[:number]:
        print(i['番号']+','+i['名字'])