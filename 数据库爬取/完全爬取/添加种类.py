#decoding=gbk
from shujuku2 import shujuku2
from methods import *
import re
general='https://2535fh.com/tag-vod-wd-'
lat='-p-1.html'


def lastfirst(url):
    a=huoquurl(url)
    b=bs(a,'lxml')
    shuliang=str(list(b.select('body > div > div > div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main > ul'))[0])
    print(shuliang)
    try:
        shuliang=re.findall('共\d+部',shuliang)[0]
        shuliang=shuliang[1:]
        shuliang=shuliang[:-1]
        print(shuliang)
    except:
        shuliang='unknown'
    return shuliang
def last(url):
    a=huoquurl(url)
    b=bs(a,'lxml')
    shuju=b.select('.lei>div>div>a')
    shuju=list(shuju)
    final=[]
    for i in shuju:
        i=str(i)
        i=re.findall('>\S+<',i)[0]
        i=i[1:]
        i=i[:-1]
        final.append(i)
    return final
        

a=last('https://2535fh.com/tags.html')

for i in a:
    url=general+i+lat
    shuliang=lastfirst(url)
    fin={'种类':i,'数量':shuliang}
    b=shujuku2(fin)
    b.xieruone()
