#decoding=gbk
import pandas
import numpy

from shujuku7 import suju
data=pandas.read_csv('juese.csv',encoding='gbk')
name=data.iloc[0:,0]
shu=data.iloc[0:,1]
fina=[]
for i,q in zip(name,shu):
    fina.append({'name':i,'shuliang':q})    #基本东西也是如此，允许自由写入与写出
a=suju(fina)
a.xierumany()