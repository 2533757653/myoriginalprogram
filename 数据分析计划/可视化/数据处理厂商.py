#decoding=gbk
from shujuku2 import shujuku
from methods import *
from pltkey import pltkey
from shujuku3 import suju
a=shujuku()
tem=a.chazhaore('����','-')
tem=list(tem)
changshang=[]
for i in tem:
    changshang.append(i['����'])
changshang=findmost(changshang)
x,y=zhuana(changshang)
for i,q in zip(x,y):
    fin={'����':i,'����':q}
    a=suju(fin)
    a.xieruone()


