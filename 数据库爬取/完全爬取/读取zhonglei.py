#decoding=gbk
import pandas
import numpy
from pltkey import pltkey
data=pandas.read_csv('zhonglei.csv',encoding='gbk')
plt=pltkey(500,50)
print(data.iloc[0:10,0]) #数据在后，也就是说，前是x，后为y
plt.setlable(5)
plt.zhexian(data.iloc[0:50,1],data.iloc[0:50,0],6)

