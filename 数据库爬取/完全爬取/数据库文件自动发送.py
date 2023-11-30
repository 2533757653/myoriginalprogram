#decoding=gbk
from mailwangyi import youjian
from shujuku import shujuku
from socketpeizhi import *
def chulifangfa():
    print('第一个是按番号，第二个按名称，第三个按类别，第四个按厂商，第五个混杂搜索')
    cho=int(input('choice:'))
    if cho==1:
        a=input('番号:')
        b=shujuku()
        final= list(b.chazhaore('番号',a))

    if cho==2:
        a=input('名称:')
        b=shujuku()
        final=list(b.chazhaore('名字',a))

    if cho==3:
        a=input('类别:')
        a=a.split(',')
        b=shujuku()
        final=list(b.chazhao('标签',{'$all':a}))

    if cho==4:
        a=input('厂商:')
        b=shujuku()
        final= list(b.chazhaore('厂商',a))

    if cho==5:
        print('请分别按大致番号，标签，类别，厂商的文本输入，如果没有请输入none，标签间用，隔开')
        li=['番号','标签','类别','厂商']
        a=input('jieguo:')
        a=a.split(' ')
        c=a[1].split(',')
        a[1]=c
        for i in range(len(a)):
            if a[i]=='none':
                a[i]=''
        b=shujuku()
        final=list(b.chazhaosuoyou(li,a))
    for i in final:
        i.pop('_id')
    return final
youjian('2533757653@qq.com',contents=chulifangfa())