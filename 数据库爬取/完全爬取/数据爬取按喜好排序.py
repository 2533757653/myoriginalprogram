#decoding=gbk
from shujuku2 import shujuku as shuju
from shujuku import shujuku
from methods import *
def chulifangfa():
    print('��һ���ǰ����ţ��ڶ��������ƣ�����������𣬵��ĸ������̣��������������')
    cho=int(input('choice:'))
    if cho==1:
        a=input('����:')
        b=shuju()
        pri(list(b.chazhaore('����',a)))

    if cho==2:
        a=input('����:')
        b=shuju()
        pri(list(b.chazhaore('����',a)))

    if cho==3:
        a=input('���:')
        a=a.split(' ')
        b=shuju()
        pri(list(b.chazhao('��ǩ',{'$all':a})))

    if cho==4:
        a=input('����:')
        b=shuju()
        pri(list(b.chazhaore('����',a)))

    if cho==5:
        print('��ֱ𰴴��·��ţ���ǩ���������֣����̵��ı����룬���û��������none����ǩ���ã�����')
        li=['����','��ǩ','����','����']
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
    return a['Ȩ��']*100
def quanzhong(lis):
    tem=0
    for i in lis:
        tem=tem+i[1]
    tem=float(tem)
    for i in lis:
        i[1]=float(i[1])/tem
    return lis
def pri(list1):
    #�Ƚ�favourite�ڵĶ���ȡ�������б��棬���Ⱥ��ٰ���Ȩ�رȽ�������Ȩ�رȰ����̺����ĸ��ʽ�����������Ȩ����ߵ���Ʒ��
    a=shujuku()
    shujub=a.chazhaore('����','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    for i in shujub:
        chang.append(i['����'])
        biao.append(i['��ǩ'])
    biao=zhuan(biao)
    chang=findmost(chang)
    biao=findmost(biao)
    biao=quanzhong(biao)
    chang=quanzhong(chang)
    for i in list1:
        qu=i['����']
        quan=float(0)
        bi=i['��ǩ']
        for t in chang:
            if qu==t[0]:
                quan=quan+t[1]
                break
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['Ȩ��']=quan
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1:
        print(i['����']+','+i['����']+'  ',end=' ')
        print(i['��ǩ'])
chulifangfa()