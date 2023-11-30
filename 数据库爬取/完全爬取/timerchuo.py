
import datetime
    
def shijian():
    with open('todaytime.txt','r') as fout:
        temtime=fout.read().split(' ')
    a=datetime.datetime(int(temtime[0]),int(temtime[1]),int(temtime[2]))
    befor=a+datetime.timedelta(days=-1)
    with open('todaytime.txt','w') as fout:
        fout.write(str(befor.year)+' '+str(befor.month)+' '+str(befor.day))
    if len(str(befor.month))<2:
        if len(str(befor.day))<2:
            return str(befor.year)+'-0'+str(befor.month)+'-0'+str(befor.day)
        else:
            return str(befor.year)+'-0'+str(befor.month)+'-'+str(befor.day)
    else:
        if len(str(befor.day))<2:
            return str(befor.year)+'-'+str(befor.month)+'-0'+str(befor.day)
        else:
            return str(befor.year)+'-'+str(befor.month)+'-'+str(befor.day)
