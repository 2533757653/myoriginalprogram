#decoding=gbk
from typing import final
from shujuku1 import shujuku
from shujuku2 import shujuku as shujukusuoyou
from methods import *
from shujuku4 import suju as shujukuchangbiao
from shujuku5 import suju as shujukujuesebiao
from shujuku6 import suju as shujukufanhaobiao
from shujuku8 import suju
import re           #ע�⣺�ڴ������һ�㣬��final���ɾͺã��ص��Ƕ�final�ĸ��£���С��λ��������������
def sor(a):
    return a[1]

def fanhaobiao(b):
    c=shujukufanhaobiao()
    shuju=[]
    shujul=list(c.chazhaore('����',b))
    for i in shujul:
         shuju.append(i['��ǩ'],i['����'])
    sorted(shuju,key=sor,reverse=True)
    return shuju
def changbiao(b):            #���е�b��ָ���������ĳ��뷬��
    c=shujukuchangbiao()
    shuju=[]
    shujul=list(c.chazhaore('����',b))
    for i in shujul:
         shuju.append(i['��ǩ'],i['����'])
    sorted(shuju,key=sor,reverse=True)
    return shuju


def biaochang(b):
    c=shujukuchangbiao()
    shuju=[]
    shujul=list(c.chazhaore('��ǩ',b))
    for i in shujul:                                         #����һ����ά�б��Ƚ�ȡϲ���ģ������ñ�ǩ���н�ȡ����������ĵط����Ӷ�����˿ںź�������Ȼ����ȡ��Ŀ����������ϲ������Ӷ��������
         shuju.append[i['����'],i['����']]
    sorted(shuju,key=sor,reverse=True)
    return shuju
def biaofanhao(b):                          #�����b����һ����ǩ�ɱ�ǩȷ����ѷ����볧��
    c=shujukufanhaobiao()
    shuju=[]
    shujul=list(c.chazhaore('��ǩ',b))
    for i in shujul:
         shuju.append[i['����'],i['����']]
    sorted(shuju,key=sor,reverse=True)       #����sort���޷�ʹ��Ȩ�أ������Ҫ��findmost����
    return shuju


def biaofanhaoliebiao(b):
    c=shujukufanhaobiao()
    shuju=[]
    shujul=[]
    for i in b:
        for q in list(c.chazhaore('��ǩ',i)):
            shujul.append(q)
    for i in shujul:
         shuju.append[i['����'],i['����']]
    sorted(shuju,key=sor,reverse=True) 
    return shuju
def biaochangliebiao(b):              
    c=shujukuchangbiao()
    shuju=[]
    shujul=[]
    for i in b:
        for q in list(c.chazhaore('��ǩ',i)):
            shujul.append(q)
    for i in shujul:
         shuju.append[i['����'],i['����']]
    sorted(shuju,key=sor,reverse=True) 
    return shuju

#����˼����ϲ�������ݶ�����������ۺ��ж������ж�������ϲ���ĸ�Ȩ�أ���Ȩ�ظ��裬�кܶ�Ȩ���ۺ��ж�
def suijichuxuan(num):
    a=shujuku()
    suoyou=shujukusuoyou()
    shujub=a.chazhaore('����','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    fanhao=[]
    for i in shujub:
        chang.append(i['����'])
        biao.append(i['��ǩ'])
        fanhao.append(i['����'].split('-')[0])
    biao=zhuan(biao)   
    chang=findmost(chang)
    biao=findmost(biao)           #��һ����ȡ����һ��
    fanhao=findmost(fanhao)
    biao=quanzhong(biao)        #����֪����ô�ã���һ��ȷ�����������������һ����Щ�����ˣ����������ϲ�����������ȡ�Ӷ�֪��ȫ������ò�Ʒ�Χ̫С
    biaomost=[biao[0][0]]


    data=list(suoyou.chazhao('��ǩ',{'$all':biaomost}))  #��һ����ɢ�����ܴ�,��Ϊ��������,���ǵ�һ����ȷ����ǩ,���ɹ�̬�ļ��������
    data=pri(data,shujub)
    return data[0:num]



def suijichuli(num):
    a=shujuku()
    data=suju()
    suoyou=shujukusuoyou()
    shujub=a.chazhaore('����','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    fanhao=[]
    for i in shujub:
        chang.append(i['����'])
        biao.append(i['��ǩ'])
        fanhao.append(i['����'].split('-')[0])
    biao=zhuan(biao)   
    chang=findmost(chang)
    biao=findmost(biao)           
    fanhao=findmost(fanhao)
    #tembiao,temchang,temfanhao=[],[],[]
    
    #for i in biao:
    #    tembiao.append(i[0])
    #for i in chang:
    #    temchang.append(i[0])
    #for i in fanhao:
    #    temfanhao.append(i[0])
    #fanhao=temfanhao
    #chang=temchang             #������֤
    #biao=tembiao     
    li=['����','����','��ǩ']
    randomzuhe=[[fanhao[0][0],chang[0][0],biao[0][0]],[fanhao[1][0],chang[0][0],biao[0][0]],[fanhao[0][0],chang[1][0],biao[0][0]],[fanhao[0][0],chang[0][0],biao[1][0]],[fanhao[0][0],chang[1][0],biao[1][0]],[fanhao[1][0],chang[1][0],biao[0][0]],[fanhao[1][0],chang[0][0],biao[1][0]],[fanhao[1][0],chang[1][0],biao[1][0]]]
    for i in randomzuhe:
        if(data.chazhaosome(li,i)):
            pass
        else:                              #����˼�������ˣ��޷�����������Ψһ��ȱ�㣬ʼ�վ��ޣ�����������һ����dataΪ���ĵĺ�����Ȼ�������������ల�ţ���һ���������ڱ�ǩ������Ϊ�����ƣ���ǩ�����������࣬Ȼ�������򣬴Ӷ��õ���࣬�����޷�ʹ��pri�����øĸ�һ��
                                        #һ�������̣�һ�������̣���������
            randomzuhe.remove(i)
    finaldata=[]
    for i in randomzuhe:
        i[2]=[i[2]]
        data=list(suoyou.chazhaosome(li,i))
        finaldata=finaldata+data
    finaldata=pri(finaldata,shujub)
    print(finaldata[0:num])
def function():
    a=[]
def suijituopan(num):
    def paixu(i):
        return i['����']
    a=shujuku()
    data=suju()
    suoyou=shujukusuoyou()
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
    #tembiao,temchang,temfanhao=[],[],[]
    
    #for i in biao:
    #    tembiao.append(i[0])
    #for i in chang:
    #    temchang.append(i[0])
    #for i in fanhao:
    #    temfanhao.append(i[0])
    #fanhao=temfanhao
    #chang=temchang             #������֤
    #biao=tembiao     
    li=['��ǩ','����']
    randomzuhe=[]
    for i in range(0,3):
        for q in range(0,3):
              tem123=[biao[q][0],chang[i][0]]                 #ֻ��ԷǷ�Ūһ�°ѣ�����ɱ�̫��
              qq=list(data.chazhaojiu(li,tem123))
              if qq:
                  randomzuhe=randomzuhe+qq
    randomzuhe=sorted(randomzuhe,key=paixu)
                             #����˼�������ˣ��޷�����������Ψһ��ȱ�㣬ʼ�վ��ޣ�����������һ����dataΪ���ĵĺ�����Ȼ�������������ల�ţ���һ���������ڱ�ǩ������Ϊ�����ƣ���ǩ�����������࣬Ȼ�������򣬴Ӷ��õ���࣬�����޷�ʹ��pri�����øĸ�һ��
                                        #һ�������̣�һ�������̣��������ɣ���һ���󵨶���
    randomzuhe=randomzuhe[:8]      
    finaldata=[]
    fanhaotem=[]
    for i in randomzuhe:
        q=[[i['��ǩ']],i['����']]
        data=list(suoyou.chazhaoever(li,q))
        for w in data:
            del w['_id']
            if w['����'] in fanhaotem:
                pass
            else:
                fanhaotem.append(w['����'])
                finaldata.append(w)
    finaldata=pri(finaldata,shujub)
    for i,q in zip(data,range(num)):
        print(i['����']+','+i['����']+'  ',end=' ')
        print(i['��ǩ'])


def biaotuozhan(num):
    a=shujuku()
    shujub=a.chazhaore('����','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    fanhao=[]
    for i in shujub:
        chang.append(i['����'])
        biao.append(i['��ǩ'])                     
        fanhao.append(i['����'].split('-')[0])
        biao=zhuan(biao)
    chang=findmost(chang)
    biao=findmost(biao)
    fanhao=findmost(fanhao)
    biao=quanzhong(biao)#����֪����ô��
    list1=[]
    c=shujukusuoyou()
    for i in biaofanhaoliebiao(biao):
           list1=list1+list(c.chazhaore('����',biao[0]))
    data=pri(list1,shujub)
    for i,q in zip(data,range(num)):
        print(i['����']+','+i['����']+'  ',end=' ')
        print(i['��ǩ'])


def jiexi1(a):
    return a['Ȩ��']*100
def pri(list1,shujub):
    #�Ƚ�favourite�ڵĶ���ȡ��,list1������������ѡ�������ݣ����б��棬���Ⱥ��ٰ���Ȩ�رȽ�������Ȩ�رȰ����̺����ĸ��ʽ�����������Ȩ����ߵ���Ʒ��
    chang=[]
    biao=[]
    listtem=[]
    list1=listtem
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
        i['Ȩ��']=quan            #���������ʱ���ĵģ����õ���
    list1=sorted(list1,key=jiexi1,reverse=True)
    return list1
def paixuhanshushixing():
    pass    #��һ������д�ľ��Ǹ�������Ĵ������,����д�ѣ�Ȩ�ؿ�����
suijituopan(18)

