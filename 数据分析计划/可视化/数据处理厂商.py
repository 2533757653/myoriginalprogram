#decoding=gbk
from shujuku2 import shujuku
from methods import *
from pltkey import pltkey
from shujuku3 import suju
a=shujuku()
tem=a.chazhaore('番号','-')
tem=list(tem)
changshang=[]
for i in tem:
    changshang.append(i['厂商'])
changshang=findmost(changshang)
x,y=zhuana(changshang)
for i,q in zip(x,y):
    fin={'厂商':i,'数量':q}
    a=suju(fin)
    a.xieruone()


