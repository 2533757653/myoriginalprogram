#decoding=gbk
from shujuku2 import shujuku2
from methods import *
import re
general='https://2535fh.com'
def nvyou(url):
    general='https://2535fh.com'
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('div>div>h4')
    k=[]
    xingming=[] 
    c=list(c)
    for i in c:
       i=str(i)
       i=i.split(' ')
       q=i[1]
       q=q[6:]
       q=q[:-1]
       q=q.replace('.html','_1.html')
       k.append(general+q)
    for i in k:
        i=i[31:]
        i=i[:-7]
        xingming.append(i)
    return xingming,k

def lastfirst(url):
    a=huoquurl(url)
    b=bs(a,'lxml')
    qian=[]
    hou=[]
    shuju=b.select('body > div > div > div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main > div.col-xs-6.col-md-10.info')
    shuliang=b.select('body > div > div > div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main > ul')
    try:
        shuju=str(list(shuju)[0])
        shuliang=str(list(shuliang)[0])
    except:
        pass
    try:
        yingwen=re.findall('英文名字\S+ \S+',shuju)[0]
        shuju=re.findall('>\S+ \S+<',shuju)
        yingwen=yingwen.split('：')[1]
    except:
        pass
    try:
        shuliang=re.findall('共\d+部',shuliang)[0]
        shuliang=shuliang[1:]
        shuliang=shuliang[:-1]
    except:
        shuliang='unknown'
    for i in shuju:
        i=i[1:]
        try:
            qian1=re.findall('\w+:',i)[0]
            hou1=re.findall(' \S+<',i)[0]
            qian1=qian1[:-1]
            hou1=hou1[:-1]
            hou1=hou1[1:]
            hou1=hou1.replace('</p>','')
        except:
            continue
        qian.append(qian1)
        hou.append(hou1)
    try:
       return qian,hou,yingwen,shuliang
    except:
        return qian,hou,None,shuliang

for i in range(41,1296):
    url=f'https://2535fh.com/nylb/{i}.html'
    mingzi,url1=nvyou(url)
    for i,q in zip(url1,mingzi):
        final={}
        qian,hou,yingwen,shuliang=lastfirst(i)
        final['名字']=q
        for i1,q1 in zip(qian,hou):
            final[i1]=q1
        final['英文名字']=yingwen
        final['影片数量']=shuliang
        a=shujuku2(final)
        a.xieruone()
