#decoding=gbk

from shujukuall import shujukuerfanbiao,shujukuerji 

b=shujukuerji()
data=list(b.chazhaoall())
finaldata=[]
for i in data:
    i=dict(i)
    fan=i['����']
    biao=i['��ǩ']
    for q,shu in zip(finaldata,range(len(finaldata))):
        if fan==q['����']:
            finaldata[shu]['��ǩ'].append({biao:i['����']})
            break
    else:
        finaldata.append({'����':fan,'��ǩ':[{biao:i['����']}]})
def xuanze(i):
    return list(i.values())[0]

for q in finaldata:
    q['��ǩ']=sorted(q['��ǩ'],key=xuanze)

a=shujukuerfanbiao(finaldata)
a.xierumany()