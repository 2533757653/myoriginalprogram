#decoding=gbk
from methods import *
from shujuku import shujuku
from pltkey import pltkey
a=shujuku()
shuju=a.chazhaore('����','-')
shuju=list(shuju)
chang=[]
juese=[]
biao=[]

for i in shuju:
    chang.append(i['����'])
    #juese.append(i['Ů��'])
    biao.append(i['��ǩ'])
#juese=zhuan(juese)
biao=zhuan(biao)
chang=findmost(chang)
biao=findmost(biao)
#findmost(juese)
cz=pltkey()
x,y=zhuana(biao)
cz.savepanduan('123.png')
cz.zhexian(x,y)
