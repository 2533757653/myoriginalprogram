#decoding=gbk

from shujukuall import shujukuerfanbiao,shujukuerji 

b=shujukuerji()
data=list(b.chazhaoall())
finaldata=[]
for i in data:
    i=dict(i)
    fan=i['番号']
    biao=i['标签']
    for q,shu in zip(finaldata,range(len(finaldata))):
        if fan==q['番号']:
            finaldata[shu]['标签'].append({biao:i['数量']})
            break
    else:
        finaldata.append({'番号':fan,'标签':[{biao:i['数量']}]})
def xuanze(i):
    return list(i.values())[0]

for q in finaldata:
    q['标签']=sorted(q['标签'],key=xuanze)

a=shujukuerfanbiao(finaldata)
a.xierumany()