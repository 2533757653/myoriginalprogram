#decoding=gbk
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import time
from methods import *
from shujuku2 import shujuku
from timerchuo import shijian
def apiapp1(a):
    url=f'https://cilisousuo.com/search?q={a}'
    general='https://cilisousuo.com'
    a=huoquurl(url)
    b=bs(a,'lxml')
    c=b.select('.item>.link')
    c=list(c)
    fina=[]
    final=[]
    fuzhu=0
    for i in c:
        i=str(i)
        i=i.split(' ')[2]
        i=i[6:-6]
        final.append(general+i)
    del a,b,c
    for i in final:
        time.sleep(1)
        if fuzhu==2:
            break
        try:
            a=huoquurl(i)
            b=bs(a,'lxml')
            c=b.select('input')[1]
            c=str(c)
            c=c.split(' ')[4]
            c=c[7:-3]
            fina.append(c)
            fuzhu+=1
        except:
            break
    return fina
def apiapp2(name):
    url='https://skrbtre.top/search?keyword='+name
    a=huoquurl(url)
    print(a)
    b=bs(a,'lxml')
    c=b.select('body > div > div:nth-child(6) > div.col-md-6 > ul:nth-child(2) > li:nth-child(1) > a')
    c=list(c)
    print(c)
for i in range(1,9876):
    a=shujuku()
    temtime=shijian()
    shuju=list(a.chazhaore('播出时间',temtime))
    for i in shuju:
        i.pop('_id')
        cili=apiapp1(i['番号'])
        time.sleep(0.05)
        a.update2({'番号':i['番号']},{'磁力链接':cili})

    
