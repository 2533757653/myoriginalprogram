#decoding=gbk
from shujukuall import shujukuerbiaofan,shujukuerji 
b=shujukuerji()

data=list(b.chazhaoall())
finaldata=[]
for i in data:
    i=dict(i)
    fan=i['����']
    biao=i['��ǩ']
    for q,shu in zip(finaldata,range(len(finaldata))):
        if biao==q['��ǩ']:
            finaldata[shu]['����'].append({fan:i['����']})
            break
    else:
        finaldata.append({'����':[{fan:i['����']}],'��ǩ':biao})
def xuanze(i):
    return list(i.values())[0]
for q in finaldata:
    q['����']=sorted(q['����'],key=xuanze)
a=shujukuerbiaofan(finaldata)
a.xierumany()



