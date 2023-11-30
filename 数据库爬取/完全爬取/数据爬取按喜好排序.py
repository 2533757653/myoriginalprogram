#decoding=gbk
from shujuku2 import shujuku as shuju
from shujuku import shujuku
from methods import *
def chulifangfa():
    print('第一个是按番号，第二个按名称，第三个按类别，第四个按厂商，第五个混杂搜索')
    cho=int(input('choice:'))
    if cho==1:
        a=input('番号:')
        b=shuju()
        pri(list(b.chazhaore('番号',a)))

    if cho==2:
        a=input('名称:')
        b=shuju()
        pri(list(b.chazhaore('名字',a)))

    if cho==3:
        a=input('类别:')
        a=a.split(' ')
        b=shuju()
        pri(list(b.chazhao('标签',{'$all':a})))

    if cho==4:
        a=input('厂商:')
        b=shuju()
        pri(list(b.chazhaore('厂商',a)))

    if cho==5:
        print('请分别按大致番号，标签，番号名字，厂商的文本输入，如果没有请输入none，标签间用，隔开')
        li=['番号','标签','名字','厂商']
        a=input('jieguo:')
        a=a.split(' ')
        c=a[1].split(',')
        a[1]=c
        for i in range(len(a)):
            if a[i]=='none':
                a[i]=''
        b=shuju()
        pri(list(b.chazhaosuoyou(li,a)))
def jiexi1(a):
    return a['权重']*100
def quanzhong(lis):
    tem=0
    for i in lis:
        tem=tem+i[1]
    tem=float(tem)
    for i in lis:
        i[1]=float(i[1])/tem
    return lis
def pri(list1):
    #先将favourite内的东西取出，进行保存，按先后，再按，权重比进行排序，权重比按厂商和类别的概率进行排序，优先权重最高的作品。
    a=shujuku()
    shujub=a.chazhaore('番号','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    for i in shujub:
        chang.append(i['厂商'])
        biao.append(i['标签'])
    biao=zhuan(biao)
    chang=findmost(chang)
    biao=findmost(biao)
    biao=quanzhong(biao)
    chang=quanzhong(chang)
    for i in list1:
        qu=i['厂商']
        quan=float(0)
        bi=i['标签']
        for t in chang:
            if qu==t[0]:
                quan=quan+t[1]
                break
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['权重']=quan
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1:
        print(i['番号']+','+i['名字']+'  ',end=' ')
        print(i['标签'])
chulifangfa()