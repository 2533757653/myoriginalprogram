#decoding=gbk
from shujuku import shujuku
import json
def chulifangfa():
    print('��һ���ǰ����ţ��ڶ��������ƣ�����������𣬵��ĸ������̣��������������')
    cho=int(input('choice:'))
    if cho==1:
        a=input('����:')
        b=shujuku()
        pri(list(b.chazhaore('����',a)))

    if cho==2:
        a=input('����:')
        b=shujuku()
        pri(list(b.chazhaore('����',a)))

    if cho==3:
        a=input('���:')
        a=a.split(',')
        b=shujuku()
        pri(list(b.chazhao('��ǩ',{'$all':a})))

    if cho==4:
        a=input('����:')
        b=shujuku()
        pri(list(b.chazhaore('����',a)))

    if cho==5:
        print('��ֱ𰴴��·��ţ���ǩ���������֣����̵��ı����룬���û��������none����ǩ���ã�����')
        li=['����','��ǩ','����','����']
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
        print(i['����']+','+i['����']+'  ',end=' ')
        print(i['��ǩ'])

#���������ʹ�ã���Ϊ�������ݷ���������
def paixu(list1):
    a=readjson()
    tags=[]
    chang=[]
    for i in list1:
        print(i)
    try:
       for i in a['����']:
          chang.append(i)
       for i in a['��ǩ']:
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
    print('���ǳ���ɸѡ')
    for i in zonghe:
        for q in i['��ǩ']:
            if q == tag1:
                tagd1.append(i)
                break
    for i in tagd1:
        print(i)
    print()
def paixum(chang,zonghe):
    chang1=most(chang)
    changd1=[]
    print('���Ǳ�ǩɸѡ')
    for i in zonghe:
        for q in i['��ǩ']:
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