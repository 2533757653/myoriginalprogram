#decoding=gbk
from typing import final
from shujuku8 import suju
from shujuku2 import shujuku
import re
a=shujuku()
shuju=list(a.chazhaore('����','-'))
for i in shuju:
    i.pop('_id')
finaldata=[]
for i in shuju:
    fan=i['����'].split('-')[0]
    biao=i['��ǩ']
    chang=i['����']
    for q in biao:
        data={'����':fan,'��ǩ':q,'����':chang}
        for w,i in zip(finaldata,range(len(finaldata))):
            if w['����']==fan and w['��ǩ']==q and w['����']==chang:
                w['����']+=1
                finaldata[i]==w
                break
        else:
            data['����']=1
            finaldata.append(data)
else:
    b=suju(finaldata)
    b.xierumany()

        