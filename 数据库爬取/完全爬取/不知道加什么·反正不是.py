#decoding=gbk
from shujuku4 import shujuku
from methods import *
import re
import time
general='https://2535fh.com'
def fanhao(url):
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('tbody>tr>.td2>a')
    f=b.select('tbody>tr>.td4')
    c1=b.select('tbody>tr>td')
    k=[]
    tim=[]
    fan=[]
    fuzhu=0
    f=list(f)
    c=list(c)
    for i,q in zip(c,f):
       i=str(i)
       q=str(q)
       ming=re.findall('>.+',i)[0]
       ming=ming[1:]
       ming=ming[:-4]
       chang=re.findall('>.+',q)[0]
       chang=chang[1:]
       chang=chang[:-5]
       i=i.split(' ')
       q=i[1]
       q=q[6:]
       q=q[:-1]
       f=i[1]
       f=f[6:]
       f=f[14:]
       f=f[:-6]
       for i in range(5):
           if i==2:
               i1=c1[i+fuzhu*5]
           if i==4:
               i2=c1[i+fuzhu*5]
       i1=str(i1)
       i2=str(i2)
       i1=i1[4:]
       i1=i1[:-5]
       i2=i2[4:]
       i2=i2[:-6]
       fuzhu+=1
       tim.append(i1)
       k.append(general+q) 
       fan.append(f)
    return k,tim,fan
def lastpage(url):
    zidian={'tag':[]}
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('.info>p>.genre>a')
    c=list(c)
    for tags in c:
        tags=str(tags)
        try:
           excee=re.findall('>\D+<',tags)[0]
        except:
            continue
        excee=excee[1:]
        excee=excee[:-1]
        zidian['tag'].append(excee)
    return zidian
for i in range(1,9870):
   s,t,f=fanhao(f'https://2535fh.com/fhlb/1_{i}.html')
   time.sleep(1)
   for q,t1,f1 in zip(s,t,f):
       tem=lastpage(q)
       a=shujuku()
       a.update2({'番号':f1},{'标签':tem['tag']})
       a.update2({'番号':f1},{'播出时间':t1})
       time.sleep(0.04)