#decoding=gbk
from shujuku1 import shujuku
from shujuku2 import shujuku as shujukusuoyou
from methods import *
from shujuku8 import suju
import re           #ע�⣺�ڴ������һ�㣬��final���ɾͺã��ص��Ƕ�final�ĸ��£���С��λ��������������
def sor(a):
    return a[1]
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


def tuijianqiang(num):
    def paixu(i):
        return i['����']
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
    li1=['����','��ǩ','����']
    randomzuhe=[]

    for i in range(0,3):
        for q in range(0,3):
            for w in range(0,3):
               tem123=[fanhao[w][0],biao[q][0],chang[i][0]]                
               qq=list(data.chazhaosome(li1,tem123))              #����Ǻ��ɸѡ��ȷ����Χ
               if qq:                                    
                   randomzuhe=randomzuhe+qq

    randomzuhe=sorted(randomzuhe,key=paixu,reverse=True)
                             #����˼�������ˣ��޷�����������Ψһ��ȱ�㣬ʼ�վ��ޣ�����������һ����dataΪ���ĵĺ�����Ȼ�������������ల�ţ���һ���������ڱ�ǩ������Ϊ�����ƣ���ǩ�����������࣬Ȼ�������򣬴Ӷ��õ���࣬�����޷�ʹ��pri�����øĸ�һ��
                                        #һ�������̣�һ�������̣��������ɣ���һ���󵨶���
    randomzuhe=randomzuhe[:8]      
    finaldata=[]
    fanhaotem=[]
    for i in randomzuhe:
        q=[i['����'],[i['��ǩ']],i['����']]
        data=list(suoyou.chazhaosome(li1,q))
        for w in data:
            del w['_id']
            if w['����'] in fanhaotem:
                pass
            else:
                for sw in shujub:
                    if sw['����']==w['����']:
                        break
                else:
                    fanhaotem.append(w['����'])                 #�����΢��ɸѡ
                    finaldata.append(w)      #��һ���ķ�ʱ�����������,

    finaldata=paixuhanshushixing(finaldata,shujub)
    for i,q in zip(finaldata,range(num)):
        print(i['����']+','+i['����']+'  ',end=' ')
        print(i['��ǩ'])


def tuijianruo(num):
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
    li=['��ǩ','����']
    randomzuhe=[]
    for i in range(0,3):
        for q in range(0,3):
              tem123=[biao[q][0],chang[i][0]]                 #ֻ��ԷǷ�Ūһ�°ѣ�����ɱ�̫��
              qq=list(data.chazhaojiu(li,tem123))              #����Ǻ��ɸѡ��ȷ����Χ,���ɸѡ�ô�����ɸѡ����󣬵���ȱ����������̫��
              if qq:                                    
                  randomzuhe=randomzuhe+qq

    randomzuhe=sorted(randomzuhe,key=paixu,reverse=True)
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
                for sw in shujub:
                    if sw['����']==w['����']:
                        break
                else:
                    fanhaotem.append(w['����'])                 #�����΢��ɸѡ
                    finaldata.append(w)      #��һ���ķ�ʱ�����������,

    finaldata=paixuhanshushixing(finaldata,shujub)
    for i,q in zip(finaldata,range(num)):
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
        quan=float(0)             #��������򻷽� 
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
def paixuhanshushixing(list1,shujub):
    #list1�����Ѿ�ʹ�õ����ݣ�shujub����ϲ��������,���������л��ְ�
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
                    continue
        i['Ȩ��']=quan            #���������ʱ���ĵģ����õ���
    list1=sorted(list1,key=jiexi1,reverse=True)
    return list1  
tuijianqiang(10)
tuijianruo(10)   #һ��ָ��۷�Χǿ����񣬻��и����⣬���Ƿ��ϸ�����������������������û��,������ɸѡ�Ͽ��Ը���ϸ�£�����ϲ��������Ϊ���Ӷ�Ĳο����´ΰ�
