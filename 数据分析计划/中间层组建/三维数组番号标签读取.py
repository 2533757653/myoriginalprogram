#decoding=gbk
from shujuku6 import suju
from shujuku2 import shujuku
import re
a=shujuku()
shuju=list(a.chazhaore('番号','-'))
for i in shuju:
    i.pop('_id')
b=suju()
finaldata=[]
for i in shuju:
    fan=i['番号'].split('-')[0]
    biao=i['标签']
    for q in biao:
        data={'番号':fan,'标签':q}
        for w,i in zip(finaldata,range(len(finaldata))):
            if w['番号']==fan and w['标签']==q:
                w['数量']+=1
                finaldata[i]==w
                break
        else:
            data['数量']=1
            finaldata.append(data)
else:
    b=suju(finaldata)
    b.xierumany()
