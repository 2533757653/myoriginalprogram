#decoding=gbk
from shujukuall import shujukuquanbu,shujukuchangshi
import re
from methods import *
from itertools import product
a=shujukuquanbu()

finaldata=[]
def last(url):
    a=huoquurl(url)
    b=bs(a,'lxml')
    shuju=b.select('.lei>div>div>a')
    shuju=list(shuju)
    final=[]
    for i in shuju:
        i=str(i)
        i=re.findall('>\S+<',i)[0]
        i=i[1:]
        i=i[:-1]
        final.append(i)
    return final
l=last('https://2535fh.com/tags.html')
data=list(product(l, l))
dataanother=[]
for i in data:
    if i[0]==i[1]:
        continue
    else:
        dataanother.append(i)
data=dataanother
for i in data:
    shuju=list(a.chazhaobiao('��ǩ',list(i)))
    fanhao={'����':[],'��ǩ':i}
    for q in shuju:
        fan=q['����'].split('-')[0]
        for w,shu in zip(fanhao['����'],range(len(fanhao['����']))):
            if fan==w[0]:
                fanhao['����'][shu][1]+=1
                break
        else:
            fanhao['����'].append([fan,1])
    finaldata.append(fanhao)
b=shujukuchangshi(finaldata)
b.xierumany()
