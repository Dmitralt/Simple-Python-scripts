import pymongo
from bson.objectid import ObjectId


def CUSTOMERS_POST(mydb,data):
    mycol = mydb["customers"]
    mongo_obj={} 
    for x in data["request_json"].keys():        
        mongo_obj[x]=data["request_json"][x]
    mongo_obj["птица"]=data["url_params"]["bird_name"]
    x = mycol.insert_one(mongo_obj)
    returned_obj = mycol.find_one({"_id":x.inserted_id})
    returned_obj["_id"]=str(returned_obj["_id"])
    return returned_obj

def CUSTOMERS_GET(mydb,data):   
    mycol = mydb["customers"]      
    if '_id' in data["url_params"]:
        returned_obj=mycol.find_one({"_id": ObjectId(data["url_params"]["_id"])})
        if returned_obj==None:
            returned_obj={}
        else:
            returned_obj["_id"]=str(returned_obj["_id"])        
    else:
        returned_obj={}
        for x in mycol.find():
            x["_id"]=str(x["_id"])
            returned_obj[x["_id"]]=x
    return returned_obj
    



def CUSTOMERS_DELETE(mydb,data):   
    mycol = mydb["customers"]    
    mycol.delete_one({"_id": ObjectId(data["url_params"]["_id"])})
    answer=str(data["url_params"]["_id"])+"   weas deleted"
    return {"answer":answer}   
 
def CUSTOMERS_PUT(mydb,data):   
    mycol = mydb["customers"]     
    filter = { "_id": ObjectId(data["url_params"]["_id"]) }
    newvalues = { "$set": data["request_json"] }
    mycol.update_one(filter, newvalues) 
    cursor = mycol.find()
    returned_obj={"":""}
    for record in cursor: 
        returned_obj = record
        returned_obj["_id"]=str(returned_obj["_id"]) 
    return returned_obj
    
    
  