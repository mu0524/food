import  pymongo
import ssl

#資料庫連線
client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB", ssl=True,ssl_cert_reqs=ssl.CERT_NONE)
db = client.mytopicDB
collpig = db.twpig #確認資料集
colleva = db.evaluation
collfre = db.free
collgre = db.green

#coll.stats #確認是否連線

def selectOneForTest():
    result = list(collpig.find())   #抓資料
    return result