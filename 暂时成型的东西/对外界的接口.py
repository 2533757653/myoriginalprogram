#decoding=gbk
from mailwangyi import youjian
from shujuku import shujuku
from random�Ƽ���� import suijichuxuan
import socket
def tongxinudpfuwu():
    soc1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    soc1.bind(('0.0.0.0',7788))
    while True:
        recive, sender_info = soc1.recvfrom(1024)
        recive = recive.decode("utf-8")
        break
    soc1.close()
    return recive
def chulifangfa(cho,a):
    if cho==1:
        b=shujuku()
        final= list(b.chazhaore('����',a))
    if cho==2:
        b=shujuku()
        final=list(b.chazhaore('����',a))
    if cho==3:
        a=a.split(',')  #����ǶԵģ���Ϊ�����һ�㿿�б���֧��
        b=shujuku()
        final=list(b.chazhao('��ǩ',{'$all':a}))
    if cho==4:
        b=shujuku()
        final= list(b.chazhaore('����',a))
    if cho==5:
        li=['����','��ǩ','���','����']
        a=a.split(' ')
        c=a[1].split(',')
        a[1]=c
        for i in range(len(a)):
            if a[i]=='none':
                a[i]=''
        b=shujuku()
        final=list(b.chazhaosuoyou(li,a))
    if cho==6:
        final=list(suijichuxuan(int(a)))
    for i in final:
        i.pop('_id')
    return final
def pingti(fanhao):
    b=shujuku()
    final= list(b.chazhaore('����',fanhao))
    for i in final:
        i.pop('_id')
    return final
while True:
    xinxi=tongxinudpfuwu()
    xuanze,shuju=xinxi.split(' ')[0],xinxi.split(' ')[1]
    xuanze=int(xuanze)
    data=chulifangfa(xuanze,shuju)
    youjian('2533757653@qq.com',contents=data)