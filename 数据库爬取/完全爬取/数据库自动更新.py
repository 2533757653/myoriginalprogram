#decoding=gbk
from shujuku import *
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re
from methods import *
import socket
general='https://2535fh.com'
def fanhao(url):
    fuzhu=0
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('tbody>tr>.td2>a')
    f=b.select('tbody>tr>.td4')
    c1=b.select('tbody>tr>td')
    k=[]
    dizhi=[]
    f=list(f)
    c=list(c)
    c1=list(c1)
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
       q=q[14:]
       q=q[:-6]
       f=i[1]
       f=f[6:]
       f=f[:-1]
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
       t1={'名字':ming,'厂商':chang,'番号':q,'播出时间':i1,'演出时间':i2}
       fuzhu+=1
       k.append(t1)
       dizhi.append(general+f)
    return k,dizhi
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
def final():
    fuzhu=1
    zhizh=1
    while zhizh==1:
        xinxi,dizhi=fanhao(f'https://2535fh.com/fhlb/1_{fuzhu}.html')
        shuju=shujuku()
        for i,q in zip(xinxi,dizhi):
            tags=lastpage(q)['tag']
            if list(shuju.chazhao('番号',i['番号'])):
                print('error')
                continue
            else:
                i['标签']=tags
                tem=shujuku(i)
                tem.xieruone()
        fuzhu+=1
final()






