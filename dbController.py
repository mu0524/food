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
collnews_e = db.news_etoday

#coll.stats #確認是否連線

def selectPigdata():
    result = collpig.find({},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})  #抓資料
    #result = [ {**item, **{"_id": str(item["_id"])} } for item in result ] #處理 objectId 轉string
    result = [ {**item } for item in result ] #處理 objectId 轉string
    return result

def selectGreenData():
    result = collgre.find({},{"_id":0,"market_name":1,"addr":1,"Lontitude": 1,"Latitude": 1,"Tel":1,"context":1})  #抓資料
    result = [ {**item } for item in result ] #處理 objectId 轉string
    return result

def selectFreeData():
    result = collfre.find({},{"_id":0,"market_name":1,"addr":1,"Lontitude": 1,"Latitude": 1,"context":1,"Tel":1})  #抓資料
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

#更新密碼
def updateUser(email,pwd):
    colluser.update_one({'email': email},{"$set": { 'pwd': pwd }})
    return True

def selectMaterial():
    result = collmat.find_one()
    return result

def myfind(keyWord):
    resultPig=[]
    resultGre=[]
    resultFre=[]

    #myKeyword是要搜尋的字元，到時候要POST進來
    myKeyword=keyWord

    if "台" in myKeyword:
        myKeyword2=myKeyword.replace("台","臺")

    if "臺"in myKeyword:
        myKeyword2=myKeyword.replace("臺","台")


    #豬
    myfind=collpig.find({"$or":[{"market_name":{"$regex":myKeyword}},{"addr":{"$regex":myKeyword}}]},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})
    resultPig=[ {**item } for item in myfind ]
    #綠色
    myfind=collgre.find({"$or":[{"market_name":{"$regex":myKeyword}},{"addr":{"$regex":myKeyword}}]},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})
    resultGre=[ {**item } for item in myfind ]
    #免費
    myfind=collfre.find({"$or":[{"market_name":{"$regex":myKeyword}},{"addr":{"$regex":myKeyword}}]},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})
    resultFre=[ {**item } for item in myfind ]


    if "myKeyword2" in locals():
        #豬
        myfind=collpig.find({"$or":[{"market_name":{"$regex":myKeyword2}},{"addr":{"$regex":myKeyword2}}]},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})
        resultPig+=[ {**item } for item in myfind ]
        #綠色
        myfind=collgre.find({"$or":[{"market_name":{"$regex":myKeyword}},{"addr":{"$regex":myKeyword}}]},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})
        resultGre+=[ {**item } for item in myfind ]
        #免費
        myfind=collfre.find({"$or":[{"market_name":{"$regex":myKeyword}},{"addr":{"$regex":myKeyword}}]},{"_id":0,"market_name":1,"addr":1,"Latitude": 1,"Lontitude": 1,"context":1,"Tel":1})
        resultFre+=[ {**item } for item in myfind ]

    
    return resultPig,resultGre,resultFre #接收資料時，用a,b,c就可以分別抓到資料

def selectNews_etoday():
    result = collnews_e.find()  #抓資料
    result = [ {**item, **{"_id": str(item["_id"])} } for item in result ] #處理 objectId 轉string
    return result