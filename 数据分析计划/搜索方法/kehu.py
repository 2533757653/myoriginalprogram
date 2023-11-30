#decoding=gbk
from shujukuall import shujukukehu,shujukuallstar,shujukuquanbu
from random推间 import *
from 实际排序函数 import *
from mailwangyi import youjian
class kehu:
    def __init__(self,zhanghao,mima):
        self.shujuku=shujukukehu()
        self.zonghe= shujukuallstar()
        data=self.shujuku.chazhaokehu(zhanghao,mima)
        if data:
            data=list(data)[0]
            self.fanhao=data['番号信息']
            self.biaoqian=data['标签信息']
            self.tuijian=data['推荐番号']
        else:
            print('无此用户信息！')
    def randomtui(self):
        randomtuijian(self.biaoqian)
    def star(self,fanhao):
        self.zonghe.jiaxing(fanhao)
        self.shujuku.tianjia(fanhao)         #这个地方暂时不定，因为不知道数据会怎么传回来
    def kenengxihuan(self):
        data=randomtui(self.biaoqian)
        self.tuijian=data[:20]
        self.shujuku.jiarutuijian(data[:20])
    def tuijianpaixu(self):
        prileishiyong(self.biaoqian,self.tuijian,20)
    def tuijianyouxiang(self):
        youjian(res='2533757653@qq.com',contents=self.tuijian)
    def chulifangfa(self,a):
           priyiban(self.biaoqian,a,25)    
def zhuce(zhanghu,mima):
    shujuku=shujukukehu({"_id": zhanghu,"密码": mima,"标签信息": [],"番号信息": [],'推荐番号':[]})
    shujuku.xieruone()
def tianjiaxihuan(a):
    while True:
        b=input('xihuan:')
        if b=='0':
            break
        a.star(b)
    a.kenengxihuan()
def chafan(a):
    print('第一个是按番号，第二个按名称，第三个按类别，第四个按厂商，第五个混杂搜索')
    cho=int(input('choice:'))
    if cho==1:
        an=input('番号:')
        b=shujukuquanbu()
        b=list(b.chazhaore('番号',an))

    if cho==2:
        an=input('名称:')
        b=shujukuquanbu()
        b=list(b.chazhaore('名字',an))

    if cho==3:
        an=input('类别:')
        an=an.split(',')
        b=shujukuquanbu()
        b=list(b.chazhao('标签',{'$all':an}))

    if cho==4:
        an=input('厂商:')
        b=shujukuquanbu()
        b=list(b.chazhaore('厂商',an))

    if cho==5:
        print('请分别按大致番号，标签，番号名字，厂商的文本输入，如果没有请输入none，标签间用，隔开')
        li=['番号','标签','名字','厂商']
        an=input('jieguo:')
        an=an.split(' ')
        c=an[1].split(',')
        an[1]=c
        for i in range(len(an)):
            if an[i]=='none':
                an[i]=''
        b=shujukuquanbu()
        b=b.chazhaosuoyou(li,an)
    if cho==6:
        an=input('女优:')
        b=shujukuquanbu()
        b=list(b.chazhao('女优',{'$all':[an]}))
    a.chulifangfa(b)
def denglucaozuo(zhang='2227405050',password='TJh20040226'):
    a=kehu(zhang,password)
    print('1:添加,2：推荐并发送,3:查找')
    c=input('choice:')
    if c=='1':
        tianjiaxihuan(a)
    if c=='2':
        a.tuijianyouxiang()

    if c=='3':
        chafan(a)
    if c=='4':
        a.tuijianpaixu()
denglucaozuo()

       
