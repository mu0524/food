import  pymongo
from bson.objectid import ObjectId
import json

client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB")
db = client.mytopicDB
coll = db.twpig #確認資料集
#coll = db.free
#coll = db.green


#測試用資料庫
# client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB")
# db = client.mytryQAQ
# coll = db.pigpig #確認資料集

coll.stats #確認是否連線


with open('D:\\git_workplace\\food\\material\\data_pig.json', newline='',encoding = 'utf8') as jsonfile: #注意路徑
    data = json.load(jsonfile)

#台灣豬適用，去除所有換行
"""
a=0
for elem in data:
    elem["market_name"]=elem["market_name"].replace("\n","")
    elem["context"]=elem["context"].replace("\n","")
    elem["addr"]=elem["addr"].replace("\n","")
    a+=1
    if a%80==0:
        print("*",end="")
"""

if isinstance(data, list):
    coll.insert_many(data)
else:
    coll.insert_one(data)

print("OK~")

"""
#寫資料庫的find可以參考
result = list(collpig.find({"market_name": {"$regex":"快車肉乾"}}))
for element in result:
    print(element)
    print("\n\n\n\n\n")"""