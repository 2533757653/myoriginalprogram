import numpy
def findmost(lis):
    List_set = set(lis)
    fina=[]
    for item in List_set:
        fina.append([item, lis.count(item)])
    fina=sorted(fina,key=jiexi,reverse=True)
    return fina
def jiexi(a):
    return a[1]
def zhuan(lis):
    final=[]
    for i in lis:
        for q in i:
            final.append(q)
    return final
def zhuan1(lis):
    final=[]
    for i in lis:
        for q in i:
            final.append(q)
    return final
def zhuana(lis):
    x=[]
    y=[]
    for i in lis:
        x.append(i[0])
        y.append(i[1])
    return x,y
def quanzhong(lis):
    tem=0
    for i in lis:
        tem=tem+i[1]
    for i in lis:
        i[1]=i[1]/tem
    return lis
def quanzhongsorted(lis):
    tem=0
    for i in lis:
        tem=tem+i[1]
    for i in lis:
        i[1]=i[1]/tem
    lis=sorted(lis,key=jiexi,reverse=True)
    return lis[0]
def sortsanwei(x,y):
    zonghe=[]#x 表示厂商，y表示数量
    x1=[]
    y1=[]
    for i,q in zip(x,y):
        zonghe.append([i,q])
    zonghe=sorted(zonghe,key=jiexi,reverse=True)
    for i in zonghe:
        y1.append(i[1])
        x1.append(i[0])
    return x1,y1
def zhongweijunzhi(da1): #这个里面全是数字
    for i in range(len(da1)):
        if i%2==1:
            if da1[i//2]+1>numpy.mean(da1[:i]):
                break
        else:
            if (da1[i//2]+da1[i//2+1])//2>numpy.mean(da1[:i]):               #就是知道突然突起的函数
                break
    return i//2



