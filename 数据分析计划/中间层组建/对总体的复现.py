#decoding=gbk
from shujukuall import shujukuquanbu,shujukuallstar
a=shujukuquanbu()
data=list(a.chazhaore('番号','-'))
final=[]
tem={'CETD-226'}
for i in data:
    fanhao=i['番号']
    tem.add(fanhao)
for i in tem:
    final.append({'_id':i,'star':0})
b=shujukuallstar(final)
b.xierumany()             #切，早知道直接用——id作为番号地址了，不至于这么麻烦