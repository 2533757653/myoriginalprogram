#decoding=gbk
from methods import *
from shujuku import shujuku
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re
import time
from methods import *
hou='.html'
gener='https://www.xfhku.com/daquan'
tem=0
cun='/index_'
def jpgfanhao(url):
    a=huoquurl(url)  #获取图片url与名称
    b=bs(a,'lxml')
    final=[]
    img=b.select('.a_cover')
    img=list(img)
    for im in img:
        im=str(im)
        mi=im.split(' ')[2]
        im=im.split(' ')[4]
        try:
            mi=re.findall('="\S+"',mi)[0]
            mi=mi[2:]
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
        tem=[mi,im]
        final.append(tem)
    return final
nianfen=[2014,2015,2016,2017,2018,2019,2020]
shijian=[76,104,182,218,174,71,8]

for nian,shi in zip(nianfen,shijian):
        for i in range(1,shi):
            if i==1:
                url=gener+str(nian)+'/'
            else:
                url=gener+str(nian)+cun+str(i)
            shuju=jpgfanhao(url)
            a=shujuku()
            time.sleep(1)
            for i in shuju:
                with open(f'C:\\tupian\\fanhao\\{i[0]}.jpg','wb') as fout:
                    try:
                        fout.write(huoqutu('https:'+i[1]))
                    except:
                        print(i[0])
                        continue
                a.update2({'番号':i[0]},{'位置':f'C:\\tupian\fanhao\{i[0]}.jpg'})
                time.sleep(0.06)
