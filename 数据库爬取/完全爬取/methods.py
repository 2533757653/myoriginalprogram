#decoding=gbk
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from requests_html import HTMLSession
def huoquurl(url,text=''):
     ua = UserAgent()
     hea = {
        'User-Agent': ua.random}
     cok={}
     if text!='':
         text=text.split(';')
         for i in range(len(text)):
           tem=text[i].split('=')
           cok[tem[0]]=tem[1]
     try:
        r = requests.get(url,headers=hea,timeout=30,cookies=cok)
        r.raise_for_status()  
        r.encoding = r.apparent_encoding
        return r.text
     except:
        return "产生异常"
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
def newhuoqu(url,session):
    ua = UserAgent()
    hea = {
        'User-Agent': ua.random}
    cok={}
    if text!='':
         text=text.split(';')
         for i in range(len(text)):
           tem=text[i].split('=')
           cok[tem[0]]=tem[1]
    try:
       session.get(url,headers=hea,timeout=30)
       return session.html
    except:
       print('wrong',url)

def shujuchuli(session,xpat):
    return session.xpath(xpat)
def wenben(qian,hou):
    b=bs(qian,'lxml')
    c=b.select(hou)
    return c
def write(path,content):
    with open(path,'wb') as fout:
        fout.write(content)

def huoquurljiandan(url,hea,text=''):
     cok={}
     if text!='':
         text=text.split(';')
         for i in range(len(text)):
           tem=text[i].split('=')
           cok[tem[0]]=tem[1]
     try:
        r = requests.get(url,headers=hea,timeout=30,cookies=text)
        r.raise_for_status()  
        r.encoding = r.apparent_encoding
        return r.text
     except:
        return "产生异常"
def huoquurlzizu(url,header,text=''):
     ua = UserAgent()
     header=header.split(';')
     hea = {}
     for i in header:
         i=i.split(':')
         hea[i[0]]=i[1]
     cok={}
     if text!='':
         text=text.split(';')
         for i in range(len(text)):
           tem=text[i].split('=')
           cok[tem[0]]=tem[1]
     try:
        r = requests.get(url,headers=hea,timeout=30,cookies=cok)
        r.raise_for_status()  
        r.encoding = r.apparent_encoding
        return r.text
     except:
        return "产生异常"
def liurequest(url):
     r = requests.get(url,stream=True,timeout=30)
     return r.text