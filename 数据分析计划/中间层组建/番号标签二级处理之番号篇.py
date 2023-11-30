#decoding=gbk
from shujukuall import shujukuerbiaofan,shujukuerji 
b=shujukuerji()

data=list(b.chazhaoall())
finaldata=[]
for i in data:
    i=dict(i)
    fan=i['番号']
    biao=i['标签']
    for q,shu in zip(finaldata,range(len(finaldata))):
        if biao==q['标签']:
            finaldata[shu]['番号'].append({fan:i['数量']})
            break
    else:
        finaldata.append({'番号':[{fan:i['数量']}],'标签':biao})
def xuanze(i):
    return list(i.values())[0]
for q in finaldata:
    q['番号']=sorted(q['番号'],key=xuanze)
a=shujukuerbiaofan(finaldata)
a.xierumany()



