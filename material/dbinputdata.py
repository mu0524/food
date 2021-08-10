import  pymongo
from bson.objectid import ObjectId
import json

client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB")
db = client.mytopicDB
coll = db.twpig #確認資料集
#coll = db.evaluation
#coll = db.free
#coll = db.green


coll.stats #確認是否連線


with open('D:\\git_workplace\\food\\program\\data_pig.json', newline='',encoding = 'utf8') as jsonfile: #注意路徑
    data = json.load(jsonfile)

print(data)

if isinstance(data, list):
    coll.insert_many(data)  
else:
    coll.insert_one(data)


