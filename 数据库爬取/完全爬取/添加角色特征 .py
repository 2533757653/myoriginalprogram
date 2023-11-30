#decoding=gbk
from shujuku2 import shujuku
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re
import time
from methods import *
general='https://2535fh.com'
def fanhao(url,ming):
    fuzhu=0
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('tbody>tr>.td2>a')
    f=b.select('tbody>tr>.td4')
    c1=b.select('tbody>tr>td')
    k=[]
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
       try:
          q=re.findall('/\w+-\d+',q)[0]
       except:
          print(q)
          continue
       q=q[1:]
       k.append(q)
    a=shujuku()
    for i in k:                       #这是在说我搞得可以，但是爬取的不行，
        qw=list(a.chazhaore('番号',i))
        if qw:
            if qw[0]['女优']:
                a.update2({'番号':i},{'女优':qw[0]['女优'].append(ming)})
            else:
                a.update2({'番号':i},{'女优':[ming]})

def nvyou(url):
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('div>div>h4')
    hou='.html'
    k=[]
    c=list(c)
    for i in c:
       i=str(i)
       i=i.split(' ')
       q=i[1]
       q=q[6:]
       q=q[:-1]
       q=q.replace('.html','_1.html')
       k.append(general+q)
       #k里面是角色名称
    for i in k:
        a=huoquurl(i)
        mingzi=i[31:]
        mingzi=mingzi[:-7]
        b=bs(a,'lxml')
        shuliang=b.select('body > div > div > div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main > ul')
        try:
            shuliang=str(list(shuliang)[0])
        except:
            pass
        try:
            shuliang=re.findall('共\d+部',shuliang)[0]
            shuliang=shuliang[1:]
            shuliang=shuliang[:-1]
            shuliang=int(shuliang)
        except:
            shuliang=1
        for w in range(1,shuliang):
            tem=i[:-6]+str(w)+hou
            fanhao(tem,mingzi)
for i in range(1,10000):
    url='https://2535fh.com/nylb/'
    another='.html'
    nvyou(url+str(i)+another)
