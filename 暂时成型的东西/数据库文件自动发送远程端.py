#decoding=gbk
from mailwangyi import youjian
from shujuku import shujuku
from socketpeizhi import *
from random推荐组合 import suijichuxuan
def chulifangfa(cho,a):
    if cho==1:
        b=shujuku()
        final= list(b.chazhaore('番号',a))
    if cho==2:
        b=shujuku()
        final=list(b.chazhaore('名字',a))
    if cho==3:
        a=a.split(',')  #这个是对的，因为输入的一般靠列表来支持
        b=shujuku()
        final=list(b.chazhao('标签',{'$all':a}))
    if cho==4:
        b=shujuku()
        final= list(b.chazhaore('厂商',a))
    if cho==5:
        li=['番号','标签','类别','厂商']
        a=a.split(' ')
        c=a[1].split(',')
        a[1]=c
        for i in range(len(a)):
            if a[i]=='none':
                a[i]=''
        b=shujuku()
        final=list(b.chazhaosuoyou(li,a))
    if cho==6:
        suijichuxuan(a)
    for i in final:
        i.pop('_id')
    return final
def pingti(fanhao):
    b=shujuku()
    final= list(b.chazhaore('番号',fanhao))
    for i in final:
        i.pop('_id')
    return final
while True:
    xinxi=tongxinudpfuwu()
    xuanze,shuju=xinxi.split(' ')[0],xinxi.split(' ')[1]
    xuanze=int(xuanze)
    youjian('2533757653@qq.com',contents=chulifangfa(xuanze,shuju))