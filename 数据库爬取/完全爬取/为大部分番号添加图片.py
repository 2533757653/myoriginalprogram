#decoding=gbk
from methods import *
from shujuku3 import shujuku
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re
import time
from methods import *
hou='.html'
gener='https://www.vipfhk.com/nvyou/p'
general='https://www.vipfhk.com'
def jpgfanhao(url):
    a=huoquurl(url)  #获取图片url与名称
    b=bs(a,'lxml')
    final=[]
    img=b.select('.img_post>img')
    mingzi=b.select('.link>p')
    img=list(img)
    mingzi=list(mingzi)
    for im,mi in zip(img,mingzi):
        im=str(im)
        mi=str(mi)
        im=im.split(' ')[2]
        try:
            mi=re.findall('>\S+<',mi)[0]
            mi=mi[1:]
            mi=mi[:-1]
        except:
            print('error')
            continue
        try:
            im=re.findall('="\S+"',im)[0]
            im=im[2:]
            im=im[:-1]
        except:
            print('error')
            continue
        im=general+im
        tem=[mi,im]
        final.append(tem)
    return final
hou='.html'
gener='https://www.vipfhk.com/nvyou/p'
def huoqutu(url):
    ua = UserAgent()
    hea = {
        'User-Agent': ua.random}
    try:
        a = requests.get(url=url, headers=hea,timeout=30)
        a.raise_for_status()
        a.encoding = a.apparent_encoding
        return a.content
    except:
        print('产生异常')
for i in range(1,1032):
    url=gener+str(i)+hou
    shuju=jpgfanhao(url)
    a=shujuku()
    time.sleep(1)
    for i in shuju:
        with open(f'C:\\tupian\\juese\\{i[0]}.jpg','wb') as fout:
            try:
                fout.write(huoqutu(i[1]))
            except:
                print(i[0])
                continue
        a.update2({'名字':i[0]},{'位置':f'C:\\tupian\juese\{i[0]}.jpg'})
        time.sleep(1)