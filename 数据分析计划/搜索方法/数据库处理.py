#decoding=gbk
from shujuku import shujuku
import json
def chulifangfa():
    print('第一个是按番号，第二个按名称，第三个按类别，第四个按厂商，第五个混杂搜索')
    cho=int(input('choice:'))
    if cho==1:
        a=input('番号:')
        b=shujuku()
        pri(list(b.chazhaore('番号',a)))

    if cho==2:
        a=input('名称:')
        b=shujuku()
        pri(list(b.chazhaore('名字',a)))

    if cho==3:
        a=input('类别:')
        a=a.split(',')
        b=shujuku()
        pri(list(b.chazhao('标签',{'$all':a})))

    if cho==4:
        a=input('厂商:')
        b=shujuku()
        pri(list(b.chazhaore('厂商',a)))

    if cho==5:
        print('请分别按大致番号，标签，番号名字，厂商的文本输入，如果没有请输入none，标签间用，隔开')
        li=['番号','标签','名字','厂商']
        a=input('jieguo:')
        a=a.split(' ')
        c=a[1].split(',')
        a[1]=c
        for i in range(len(a)):
            if a[i]=='none':
                a[i]=''
        b=shujuku()
        pri(list(b.chazhaosuoyou(li,a)))
def pri(list1):
    for i in list1:
        print(i['番号']+','+i['名字']+'  ',end=' ')
        print(i['标签'])

#下面的无需使用，因为这是数据分析的内容
def paixu(list1):
    a=readjson()
    tags=[]
    chang=[]
    for i in list1:
        print(i)
    try:
       for i in a['厂商']:
          chang.append(i)
       for i in a['标签']:
           for q in i:
              tags.append(q)
       paixuc(tags,list1)
       paixum(chang,list1)
       print()
    except:
       pass
def paixuc(tags,zonghe):
    tag1=most(tags)
    tagd1=[]
    print('这是厂商筛选')
    for i in zonghe:
        for q in i['标签']:
            if q == tag1:
                tagd1.append(i)
                break
    for i in tagd1:
        print(i)
    print()
def paixum(chang,zonghe):
    chang1=most(chang)
    changd1=[]
    print('这是标签筛选')
    for i in zonghe:
        for q in i['标签']:
            if q == chang1:
                changd1.append(i)
                break
    for i in changd1:
        print(i)
def readjson():
    with open('shuju.json','r',encoding='utf-8') as fout:
         return json.load(fout)
def most(shuju):
    shujus=set(shuju)
    shuliang=[]
    for i in shujus:
        shuliang.append(shuju.count(i))
    tem=max(shuliang)
    weizhi=shuliang.index(tem)
    shujus=list(shujus)
    shuju1=shujus[weizhi]
    return shuju1

chulifangfa()