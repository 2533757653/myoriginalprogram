#decoding=gbk
import pymongo
from pymongo import MongoClient
class shujukukehu:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.�ͻ���
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 
   def chazhaokehu(self,zhanghao,mima):
       user_co=self.user
       value=user_co.find({'_id':zhanghao,'����':mima})
       self.zhanghao=zhanghao
       self.mima=mima
       self.value=value
       return value 
   def tianjia(self,fanhao):
       user_co=self.user
       user_co.update_one({'_id':self.zhanghao,'����':self.mima},{'$addToSet':{'������Ϣ':fanhao}})
       biao=list(shujukuquanbu().chazhaore('����',fanhao))[0]['��ǩ']
       user_co.update_one({'_id':self.zhanghao,'����':self.mima},{'$addToSet':{'��ǩ��Ϣ':biao}})
   def jiarutuijian(self,fanhao):
       user_co=self.user
       user_co.update_one({'_id':self.zhanghao,'����':self.mima},{'$set':{'�Ƽ�����':fanhao}})
   def export(self):
       for i in self.value:
           print(i)
class shujukuquanbu:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.ȫ��
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 
   def chazhaobiao(self,qian,hou):
       user_co=self.user
       value=user_co.find({qian:{'$all':hou}})
       self.value=value       
       return value 

   def export(self):
       for i in self.value:
           print(i)
class shujukuerji:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.�������ݿ�
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 
   def chazhaoall(self):
       user_co=self.user
       value=user_co.find()
       self.value=value
       return value 
   def export(self):
       for i in self.value:
           print(i)
class shujukuerbiaofan:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.�������ݿ���̬1���Զ��
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 

   def export(self):
       for i in self.value:
           print(i)
class shujukuerfanbiao:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.�������ݿ���̬1��Զ෬
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 

   def export(self):
       for i in self.value:
           print(i)
class shujukuchangshi:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.����
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})

        return value
   def chazhaoyidian(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$all':hou}})
 
        return value 

   def export(self):
       for i in self.value:
           print(i)

class shujukuzuichangshi:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.�����
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 

   def export(self):
       for i in self.value:
           print(i)
class shujukuallstar:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.����star
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})
   def jiaxing(self,fan):
       user_co=self.user
       value=list(user_co.find ({'_id':fan}))[0]
       user_co.update_one({'_id':fan},{'$set':{'star':int(value['star'])+1}})
       return value
   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 

   def export(self):
       for i in self.value:
           print(i)
class shujukujingjianquanbu:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.����ʽȫ��
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)

   def update1(self,content):
        user_co=self.user
        for i,q in zip(self.value,content):
           user_co.update(i,{'$set':q})
   def update2(self,path,content):
       user_co=self.user
       user_co.update_one(path,{'$set':content})

   def exportdb(self):
        client = MongoClient('mongodb://localhost:27017/')
        result = client['DB']['fanhao'].aggregate([])
        self.value=result
   def chazhao(self,qian,hou):
        user_co=self.user
        value=user_co.find ({qian:hou})
 
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
 
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
 
        return value 
   def chazhaobiao(self,qian,hou):
       user_co=self.user
       value=user_co.find({qian:{'$all':hou}})
       self.value=value       
       return value 

   def export(self):
       for i in self.value:
           print(i)
