#decoding=gbk
from mailwangyi import youjian
from shujuku import shujuku
from socketpeizhi import *
def chulifangfa():
    print('��һ���ǰ����ţ��ڶ��������ƣ�����������𣬵��ĸ������̣��������������')
    cho=int(input('choice:'))
    if cho==1:
        a=input('����:')
        b=shujuku()
        final= list(b.chazhaore('����',a))

    if cho==2:
        a=input('����:')
        b=shujuku()
        final=list(b.chazhaore('����',a))

    if cho==3:
        a=input('���:')
        a=a.split(',')
        b=shujuku()
        final=list(b.chazhao('��ǩ',{'$all':a}))

    if cho==4:
        a=input('����:')
        b=shujuku()
        final= list(b.chazhaore('����',a))

    if cho==5:
        print('��ֱ𰴴��·��ţ���ǩ����𣬳��̵��ı����룬���û��������none����ǩ���ã�����')
        li=['����','��ǩ','���','����']
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