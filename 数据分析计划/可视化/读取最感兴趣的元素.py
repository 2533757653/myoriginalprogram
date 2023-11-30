#decoding=gbk
from methods import *
from shujuku import shujuku
from pltkey import pltkey
a=shujuku()
shuju=a.chazhaore('番号','-')
shuju=list(shuju)
chang=[]
juese=[]
biao=[]

for i in shuju:
    chang.append(i['厂商'])
    #juese.append(i['女优'])
    biao.append(i['标签'])
#juese=zhuan(juese)
biao=zhuan(biao)
chang=findmost(chang)
biao=findmost(biao)
#findmost(juese)
cz=pltkey()
x,y=zhuana(biao)
cz.savepanduan('123.png')
cz.zhexian(x,y)
