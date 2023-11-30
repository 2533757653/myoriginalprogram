#decoding=gbk
from shujuku2 import shujuku
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re
import time
from methods import *
general='https://2535fh.com'
def fanhao(url):
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
       url1=i[1]
       url1=url1[6:]
       url1=url1[:-1]
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
       t1={'_id':ming,'厂商':chang,'番号':q,'播出时间':i1,'演出时间':i2,'url':general+url1}
       fuzhu+=1
       k.append(t1)
    return k
def lastpage(url):
    zidian={'tag':[],'nvyou':[]}
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('.info>p>.genre>a')
    juese=b.select('div>div>a')
    c=list(c)
    for i in juese:
        i=str(i)
        try:
            i=re.findall('title=\S+',i)[0]
        except:
            continue
        i=i[7:]
        zidian['nvyou'].append(i)
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
with open('tem.txt','r') as fout:
    tq=fout.read()
with open('yeshu.txt','r') as fout:     #新技术中断连续技术
    yici=int(fout.read())
for i in range(int(tq),11864):
   fuzhu=0
   s=fanhao(f'https://2535fh.com/fhlb/1_{i}.html')
   time.sleep(1)
   with open('tem.txt','w') as fout:
       fout.write(str(i))
   for q in s:
       if fuzhu>=yici:
            temp=0
            while True:
                tem=lastpage(q['url'])
                q['标签']=tem['tag']
                q['女优']=tem['nvyou']
                q.pop('url')
                try:
                    a=shujuku(q)
                    a.xieruone()
                except:
                    break
                if list(a.chazhao('番号',q['番号'])):
                    break
                else:
                    if temp>5:
                        print('error')
                        exit(0)
                    temp+=1
                    print('网络问题，稍后')
                    time.sleep(0.5)
            with open('yeshu.txt','w') as fout:
                fout.write(str(fuzhu))
            yici=-1
            time.sleep(0.05)
       fuzhu+=1