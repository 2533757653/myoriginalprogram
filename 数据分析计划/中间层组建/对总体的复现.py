#decoding=gbk
from shujukuall import shujukuquanbu,shujukuallstar
a=shujukuquanbu()
data=list(a.chazhaore('����','-'))
final=[]
tem={'CETD-226'}
for i in data:
    fanhao=i['����']
    tem.add(fanhao)
for i in tem:
    final.append({'_id':i,'star':0})
b=shujukuallstar(final)
b.xierumany()             #�У���֪��ֱ���á���id��Ϊ���ŵ�ַ�ˣ���������ô�鷳