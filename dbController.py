# from food.app import user
import  pymongo
import ssl

from pymongo import results

#資料庫連線
client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB", ssl=True,ssl_cert_reqs=ssl.CERT_NONE)
db = client.mytopicDB
collpig = db.twpig #確認資料集
colleva = db.evaluation
collfre = db.free
collgre = db.green
colluser = db.User

#coll.stats #確認是否連線



def selectPigdata():
    result = collpig.find()  #抓資料
    result = [ {**item, **{"_id": str(item["_id"])} } for item in result ] #處理 objectId 轉string
    return result

#找全部使用者
def selectUser(email):
    result = colluser.find({'email': email})  #抓資料
    result = [ {**item, **{"_id": str(item["_id"])} } for item in result ] #處理 objectId 轉string
    return result

#找使用者個人資訊
def selectUserInfo(email):
    result = colluser.find_one({'email': email})
    return result

#新增使用者
def insertUser(userID,email,pwd):
    colluser.insert_one({'userID': userID, 'email':email, 'pwd':pwd})
    return True
