#decoding=gbk
from pickletools import TAKEN_FROM_ARGUMENT1
import random
import matplotlib.pyplot as plt
class pltkey:
    def __init__(self,x=220,y=50):
        self.plt=plt
        self.plt.figure( figsize=(x,y), dpi=100 )
        self.plt.grid(True, linestyle='--', alpha=0.5)
        self.plt.rcParams['font.sans-serif'] = ['SimHei'] 
        self.plt.rcParams['axes.unicode_minus']=False 
        self.pan=0
        #没写完，怎么保存不知道
    def tiaoxing(self,x,y):
        self.plt.barh(x,y)
        self.save()
        self.plt.show()
    def zhuxing(self,x,y):
        self.plt.bar(x,y)
        self.save()
        self.plt.show()
    def zhexian(self,x,y,daxiao=3):
        self.plt.plot(x,y)
        for a, b in zip(x, y):
            self.plt.text(a, b, b, ha='center', va='bottom', fontsize=daxiao)
        #elf.plt.savefig(f'C:\\Users\\破晓崇明\\Pictures\\data\\{self.name}',dpi=80)
        self.plt.show()
    def mianji(self,x,y):
        self.plt.stackplot(x,y)
        self.save()
        self.plt.show()
    def sandian(self,x,y):
        self.plt.scatter(x,y)
        self.save()
        self.plt.show()
    def bingtu(self,x,y):
        self.plt.figure(figsize=(20,8), dpi=80)
        self.plt.pie(x,labels=y,autopct='%1.2f%%' )
        self.plt.legend()
        self.plt.title('the Numbers of Classes')
        self.plt.axis('equal') 
        self.save()
        self.plt.show()
    def title(self,name):
        self.title=name
    def setx(self,buchang,mingzi,min=0,max=0):
        self.plt.xticks()
        self.plt.xlabel=mingzi
        if max:
            plt.xlim((min, max))
    def sety(self,buchang,mingzi,min=0,max=0):
        self.plt.yticks()
        self.plt.ylabel=mingzi
        if max:
            plt.ylim((min, max))
        pass
    def setlable(self,daxiao):
        self.plt.tick_params(labelsize=daxiao)
        pass
    def savepanduan(self,path):
        self.pan=1
        self.name=path
    def save(self):
        if self.pan:
            self.plt.savefig(f'C:\\Users\\破晓崇明\\Pictures\\data\\{self.name}')