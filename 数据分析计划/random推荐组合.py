#decoding=gbk
from typing import final
from shujuku1 import shujuku
from shujuku2 import shujuku as shujukusuoyou
from methods import *
from shujuku4 import suju as shujukuchangbiao
from shujuku5 import suju as shujukujuesebiao
from shujuku6 import suju as shujukufanhaobiao
from shujuku8 import suju
import re           #注意：内存必须少一点，用final来干就好，重点是对final的革新，最小的位移制造最快的运行
def sor(a):
    return a[1]

def fanhaobiao(b):
    c=shujukufanhaobiao()
    shuju=[]
    shujul=list(c.chazhaore('番号',b))
    for i in shujul:
         shuju.append(i['标签'],i['数量'])
    sorted(shuju,key=sor,reverse=True)
    return shuju
def changbiao(b):            #所有的b代指显著性最大的厂与番号
    c=shujukuchangbiao()
    shuju=[]
    shujul=list(c.chazhaore('厂商',b))
    for i in shujul:
         shuju.append(i['标签'],i['数量'])
    sorted(shuju,key=sor,reverse=True)
    return shuju


def biaochang(b):
    c=shujukuchangbiao()
    shuju=[]
    shujul=list(c.chazhaore('标签',b))
    for i in shujul:                                         #建了一个四维列表，先截取喜欢的，再利用标签进行截取出最多数量的地方，从而输出端口号和数量，然后再取出目标数据利用喜好排序从而排序输出
         shuju.append[i['厂商'],i['数量']]
    sorted(shuju,key=sor,reverse=True)
    return shuju
def biaofanhao(b):                          #这里的b代表一定标签由标签确定最佳番号与厂商
    c=shujukufanhaobiao()
    shuju=[]
    shujul=list(c.chazhaore('标签',b))
    for i in shujul:
         shuju.append[i['番号'],i['数量']]
    sorted(shuju,key=sor,reverse=True)       #这种sort下无法使用权重，如果需要用findmost函数
    return shuju


def biaofanhaoliebiao(b):
    c=shujukufanhaobiao()
    shuju=[]
    shujul=[]
    for i in b:
        for q in list(c.chazhaore('标签',i)):
            shujul.append(q)
    for i in shujul:
         shuju.append[i['番号'],i['数量']]
    sorted(shuju,key=sor,reverse=True) 
    return shuju
def biaochangliebiao(b):              
    c=shujukuchangbiao()
    shuju=[]
    shujul=[]
    for i in b:
        for q in list(c.chazhaore('标签',i)):
            shujul.append(q)
    for i in shujul:
         shuju.append[i['厂商'],i['数量']]
    sorted(shuju,key=sor,reverse=True) 
    return shuju

#中心思想是喜欢和数据多的数据量来综合判断最后的判断数量，喜欢的给权重，按权重给予，有很多权重综合判断
def suijichuxuan(num):
    a=shujuku()
    suoyou=shujukusuoyou()
    shujub=a.chazhaore('番号','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    fanhao=[]
    for i in shujub:
        chang.append(i['厂商'])
        biao.append(i['标签'])
        fanhao.append(i['番号'].split('-')[0])
    biao=zhuan(biao)   
    chang=findmost(chang)
    biao=findmost(biao)           #这一步截取问题一致
    fanhao=findmost(fanhao)
    biao=quanzhong(biao)        #还不知道怎么用，这一步确定番号所有情况，这一步有些狭隘了，本意是想从喜欢的数据里获取从而知道全部，但貌似范围太小
    biaomost=[biao[0][0]]


    data=list(suoyou.chazhao('标签',{'$all':biaomost}))  #这一步耗散能量很大,分为两步进行,这是第一步，确定标签,做成固态文件读入更好
    data=pri(data,shujub)
    return data[0:num]



def suijichuli(num):
    a=shujuku()
    data=suju()
    suoyou=shujukusuoyou()
    shujub=a.chazhaore('番号','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    fanhao=[]
    for i in shujub:
        chang.append(i['厂商'])
        biao.append(i['标签'])
        fanhao.append(i['番号'].split('-')[0])
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
    #chang=temchang             #回来改证
    #biao=tembiao     
    li=['番号','厂商','标签']
    randomzuhe=[[fanhao[0][0],chang[0][0],biao[0][0]],[fanhao[1][0],chang[0][0],biao[0][0]],[fanhao[0][0],chang[1][0],biao[0][0]],[fanhao[0][0],chang[0][0],biao[1][0]],[fanhao[0][0],chang[1][0],biao[1][0]],[fanhao[1][0],chang[1][0],biao[0][0]],[fanhao[1][0],chang[0][0],biao[1][0]],[fanhao[1][0],chang[1][0],biao[1][0]]]
    for i in randomzuhe:
        if(data.chazhaosome(li,i)):
            pass
        else:                              #基本思想就是如此，无法旁生，这是唯一的缺点，始终局限，必须增加另一个以data为中心的函数，然后两个函数互相安排，另一个仅仅基于标签，不过为了限制，标签必须存在且最多，然后互相排序，从而得到最多，但是无法使用pri函数得改革一下
                                        #一个基本盘，一个开托盘，就这样吧
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
        return i['数量']
    a=shujuku()
    data=suju()
    suoyou=shujukusuoyou()
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
    #tembiao,temchang,temfanhao=[],[],[]
    
    #for i in biao:
    #    tembiao.append(i[0])
    #for i in chang:
    #    temchang.append(i[0])
    #for i in fanhao:
    #    temfanhao.append(i[0])
    #fanhao=temfanhao
    #chang=temchang             #回来改证
    #biao=tembiao     
    li=['标签','厂商']
    randomzuhe=[]
    for i in range(0,3):
        for q in range(0,3):
              tem123=[biao[q][0],chang[i][0]]                 #只针对非番弄一下把，这个成本太高
              qq=list(data.chazhaojiu(li,tem123))
              if qq:
                  randomzuhe=randomzuhe+qq
    randomzuhe=sorted(randomzuhe,key=paixu)
                             #基本思想就是如此，无法旁生，这是唯一的缺点，始终局限，必须增加另一个以data为中心的函数，然后两个函数互相安排，另一个仅仅基于标签，不过为了限制，标签必须存在且最多，然后互相排序，从而得到最多，但是无法使用pri函数得改革一下
                                        #一个基本盘，一个开托盘，就这样吧，这一个大胆多了
    randomzuhe=randomzuhe[:8]      
    finaldata=[]
    fanhaotem=[]
    for i in randomzuhe:
        q=[[i['标签']],i['厂商']]
        data=list(suoyou.chazhaoever(li,q))
        for w in data:
            del w['_id']
            if w['番号'] in fanhaotem:
                pass
            else:
                fanhaotem.append(w['番号'])
                finaldata.append(w)
    finaldata=pri(finaldata,shujub)
    for i,q in zip(data,range(num)):
        print(i['番号']+','+i['名字']+'  ',end=' ')
        print(i['标签'])


def biaotuozhan(num):
    a=shujuku()
    shujub=a.chazhaore('番号','-')
    shujub=list(shujub)
    chang=[]
    biao=[]
    fanhao=[]
    for i in shujub:
        chang.append(i['厂商'])
        biao.append(i['标签'])                     
        fanhao.append(i['番号'].split('-')[0])
        biao=zhuan(biao)
    chang=findmost(chang)
    biao=findmost(biao)
    fanhao=findmost(fanhao)
    biao=quanzhong(biao)#还不知道怎么用
    list1=[]
    c=shujukusuoyou()
    for i in biaofanhaoliebiao(biao):
           list1=list1+list(c.chazhaore('番号',biao[0]))
    data=pri(list1,shujub)
    for i,q in zip(data,range(num)):
        print(i['番号']+','+i['名字']+'  ',end=' ')
        print(i['标签'])


def jiexi1(a):
    return a['权重']*100
def pri(list1,shujub):
    #先将favourite内的东西取出,list1数据是往往是选出的数据，进行保存，按先后，再按，权重比进行排序，权重比按厂商和类别的概率进行排序，优先权重最高的作品。
    chang=[]
    biao=[]
    listtem=[]
    list1=listtem
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
        i['权重']=quan            #这个可以随时更改的，不用担心
    list1=sorted(list1,key=jiexi1,reverse=True)
    return list1
def paixuhanshushixing():
    pass    #这一处代码写的就是根据排序的代码而已,明天写把，权重可以用
suijituopan(18)

