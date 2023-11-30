#decoding=gbk
import pandas
import numpy

from shujuku7 import suju
data=pandas.read_csv('juese.csv',encoding='gbk')
name=data.iloc[0:,0]
shu=data.iloc[0:,1]
fina=[]
for i,q in zip(name,shu):
    fina.append({'name':i,'shuliang':q})
a=suju(fina)
a.xierumany()