# task from CRUD 
from pymongo import MongoClient

link =MongoClient("mongodb+srv://jk6017599:jai12345678@cluster0.mcxp1co.mongodb.net/")
mydb=link.python
col=mydb.demo
coll=mydb.sample

document=[]

document1={
       " name ":"jack",
       "age" : "3"    
                    }

document2={
 "name":"ben10",
 "age" :"10"
    }

document3={
    "name":"shinchan",
    "age":5
   }

document.append(document1)
document.append(document2)
document.append(document3)

# print(document)
# file=col.insert_many(document)
# print(file)

# file=col.update_one({"age":5},{"$set":{"age":21}})
# print(file)

# file=col.delete_one({"age":3})
# print(file)

# file=col.find().sort("name",-1)
# for i in file:
#     print(i)

# file=col.find({"age":21})
# for i in file :
#     print(i)

file=col.find().limit(3)
for i in file:
    print(i)