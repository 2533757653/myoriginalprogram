#decoding=gbk
from shujukuall import shujukukehu,shujukuallstar,shujukuquanbu
from random�Ƽ� import *
from ʵ�������� import *
from mailwangyi import youjian
class kehu:
    def __init__(self,zhanghao,mima):
        self.shujuku=shujukukehu()
        self.zonghe= shujukuallstar()
        data=self.shujuku.chazhaokehu(zhanghao,mima)
        if data:
            data=list(data)[0]
            self.fanhao=data['������Ϣ']
            self.biaoqian=data['��ǩ��Ϣ']
            self.tuijian=data['�Ƽ�����']
        else:
            print('�޴��û���Ϣ��')
    def randomtui(self):
        randomtuijian(self.biaoqian)
    def star(self,fanhao):
        self.zonghe.jiaxing(fanhao)
        self.shujuku.tianjia(fanhao)         #����ط���ʱ��������Ϊ��֪�����ݻ���ô������
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
    shujuku=shujukukehu({"_id": zhanghu,"����": mima,"��ǩ��Ϣ": [],"������Ϣ": [],'�Ƽ�����':[]})
    shujuku.xieruone()
def tianjiaxihuan(a):
    while True:
        b=input('xihuan:')
        if b=='0':
            break
        a.star(b)
    a.kenengxihuan()
def chafan(a):
    print('��һ���ǰ����ţ��ڶ��������ƣ�����������𣬵��ĸ������̣��������������')
    cho=int(input('choice:'))
    if cho==1:
        an=input('����:')
        b=shujukuquanbu()
        b=list(b.chazhaore('����',an))

    if cho==2:
        an=input('����:')
        b=shujukuquanbu()
        b=list(b.chazhaore('����',an))

    if cho==3:
        an=input('���:')
        an=an.split(',')
        b=shujukuquanbu()
        b=list(b.chazhao('��ǩ',{'$all':an}))

    if cho==4:
        an=input('����:')
        b=shujukuquanbu()
        b=list(b.chazhaore('����',an))

    if cho==5:
        print('��ֱ𰴴��·��ţ���ǩ���������֣����̵��ı����룬���û��������none����ǩ���ã�����')
        li=['����','��ǩ','����','����']
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
        an=input('Ů��:')
        b=shujukuquanbu()
        b=list(b.chazhao('Ů��',{'$all':[an]}))
    a.chulifangfa(b)
def denglucaozuo(zhang='2227405050',password='TJh20040226'):
    a=kehu(zhang,password)
    print('1:���,2���Ƽ�������,3:����')
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

       
