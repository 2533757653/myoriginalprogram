#decoding=gbk
from shujukuall import shujukuchangshi,shujukuquanbu,shujukujingjianquanbu
from methods import *
from pltkey import *
def jiexi1(a):
    return a['Ȩ��']*100
def pri(biao,shuju):
    #�Ƚ�favourite�ڵĶ���ȡ��,list1������������ѡ�������ݣ����б��棬���Ⱥ��ٰ���Ȩ�رȽ�������Ȩ�رȰ����̺����ĸ��ʽ�����������Ȩ����ߵ���Ʒ��
    #�����ŵĺֲܴڰ�,�����ֻ����̻�������
    list1=[]
    a=shujukuquanbu()
    for i in shuju[:10]:
        tem=list(a.chazhaore('����',i))
        for q in tem:
            list1.append(q)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['��ǩ']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['Ȩ��']=quan            #���������ʱ���ĵģ����õ���
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1:
        print(i['����']+','+i['����'])



def pri12(biao,shuju,number):
    #�Ƚ�favourite�ڵĶ���ȡ��,list1������������ѡ�������ݣ����б��棬���Ⱥ��ٰ���Ȩ�رȽ�������Ȩ�رȰ����̺����ĸ��ʽ�����������Ȩ����ߵ���Ʒ��
    list1=[]
    a=shujukujingjianquanbu()
    for i in shuju[:10]:
        tem=list(a.chazhaore('_id',i))
        for q in tem:
            list1.append(q)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['��ǩ']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['Ȩ��']=quan            #���������ʱ���ĵģ����õ���
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1[:number]:
        print(i['_id']+','+i['����'])

def prileishiyong(biao,shuju,number):
    #�Ƚ�favourite�ڵĶ���ȡ��,list1������������ѡ�������ݣ����б��棬���Ⱥ��ٰ���Ȩ�رȽ�������Ȩ�رȰ����̺����ĸ��ʽ�����������Ȩ����ߵ���Ʒ��
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
        bi=i['��ǩ']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['Ȩ��']=quan            #���������ʱ���ĵģ����õ���
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1[:number]:
        print(i['_id']+','+i['����'])

def priyiban(biao,shuju,number):
    list1=shuju
    biao=zhuan(biao)      
    biao=findmost(biao)
    biao=quanzhong(biao)
    for i in list1:
        quan=float(0)
        bi=i['��ǩ']
        for t in biao:
            for w in bi:
                if w==t[0]:
                    quan+=t[1]
                    break
        i['Ȩ��']=quan            #���������ʱ���ĵģ����õ���
    list1=sorted(list1,key=jiexi1,reverse=True)
    for i in list1[:number]:
        print(i['����']+','+i['����'])