#decoding=gbk
import pymongo
from pymongo import MongoClient
class suju:
   def __init__(self,content=''):
        client=pymongo.MongoClient('localhost',27017)
        db=client['DB']
        self.user=db.受欢迎
        self.content=content
        self.value=0
   def xierumany(self):
        user_co=self.user
        user_co.insert_many(self.content)
   def xieruone(self):
       user_co=self.user
       user_co.insert_one(self.content)
   def xierucontent(self,content):
       user_co=self.user
       user_co.insert_one(content)

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
        self.value=value
        return value
   def chazhaore(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian:{'$regex':hou}})
        self.value=value
        return value
   def chazhaosuoyou(self,qian,hou):
        user_co=self.user
        value=user_co.find({qian[0]:{'$regex':hou[0]},qian[1]:{'$all':hou[1]},qian[2]:{'$regex':hou[2]},qian[3]:{'$regex':hou[3]}})
        self.value=value
        return value 
   def chazhaoteding(self,qian,hou):
       user_co=self.user
       value=user_co.find({qian[0]:hou[0],qian[1]:hou[1]})
       self.value=value
       return value 
   def export(self):
       for i in self.value:
           print(i)

