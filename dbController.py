# from food.app import user
import  pymongo
import ssl

from pymongo import results

#資料庫連線
client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB", ssl=True,ssl_cert_reqs=ssl.CERT_NONE)
db = client.mytopicDB
collpig = db.twpig #確認資料集
collfre = db.free
collgre = db.green
colluser = db.User
collmat = db.material

#coll.stats #確認是否連線

def selectPigdata():
    result = collpig.find({},{"_id":0,"market_name":1,"Address":1,"Latitude": 1,"Lontitude": 1,"context":1})  #抓資料
    #result = [ {**item, **{"_id": str(item["_id"])} } for item in result ] #處理 objectId 轉string
    result = [ {**item } for item in result ] #處理 objectId 轉string
    return result

def selectGreenData():
    result = collgre.find({},{"_id":0,"Name":1,"addr":1,"Response_X": 1,"Response_Y": 1,"Tel":1})  #抓資料
    result = [ {**item } for item in result ] #處理 objectId 轉string
    return result

def selectFreeData():
    result = collfre.find({},{"_id":0,"SupplierName":1,"Address":1,"Response_X": 1,"Response_Y": 1,"GBType":1,"Tel":1})  #抓資料
    result = [ {**item } for item in result ] #處理 objectId 轉string
    return result

#找使用者
def selectUser(email):
    result = colluser.find_one({'email': email})  #抓資料
    return result

#新增使用者
def insertUser(userID,email,pwd):
    colluser.insert_one({'userID': userID, 'email':email, 'pwd':pwd})
    return True

def selectMaterial():
    result = collmat.find_one()
    return result
