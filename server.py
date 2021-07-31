from flask import Flask, Response
import flask
from flask.globals import request
import pymongo
import json
from bson.objectid import ObjectId
#---------------------------------------------------------------------------------------------------------------

try:
    mongo=pymongo.MongoClient(
        host='localhost',
        port= 27017,
        serverSelectionTimeoutMS=1000

    )
    db=mongo.Miskaa
    mongo.server_info()  # trigger exception if cannot  to db

except:
    print("ERROR- Cannot connect to db")

app = Flask(__name__)

#############################################################create---create----put---put----################################


@app.route('/users',methods=['POST'])
def create_user():
    try:
        user={'name':request.form["name"], 'last':request.form["lastname"] }
        dbResponse=db.users.insert_one(user)

        
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(response=json.dumps({"message":"user created", "id":f"{dbResponse.inserted_id}"}), status=200,mimetype='application/json')
    
    except Exception as ex:
        print('***********')
        print(ex)
        print('**********')

#####################################################################################read ---read---get---get---get ##############

@app.route("/users",methods=["GET"])                          #########GET GET GET method
def get_some_users():
    try:
        data=list(db.users.find())                           #data is cursor type so we should change it into dict or list
        for user in data:
            user["_id"]=str(user["_id"])
            
        return Response(response=json.dumps(data),status=500,mimetype='application/json')
    
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message":"cannot read users"}),status=500, mimetype='application/json' )

########################################################################################---UPDATE----UPDATE------ PATCH ----- Update

@app.route("/users/<id>",methods=["PATCH"])

def update_user(id):
    try:
        dbResponse=db.users.update_one({"_id":ObjectId(id)}, {"$set":{"name":request.form["name"]}}  )
        # for attr in dir(dbResponse):
        #     print(f"*********{attr}*****")
        if dbResponse.modified_count==1:
            return Response(response=json.dumps({"message":"user updated"}), status=200,  mimetype='application/json')
        
        return Response(response=json.dumps({"message":"nothing to update"}), status=200, mimetype='application/json')

    
    except Exception as ex:
        print("**********************")
        print(ex)
        print("**********************")
        return Response(response=json.dumps({"message":"sorry can't update user"}),status=500,mimetype='application/json')


########################################################################################delete---delete----delete---delete-----
@app.route("/users/<id>",methods=['DELETE'])

def delete_user(id):
    
    try:
        dbResponse=db.users.delete_one({"_id":ObjectId(id)})
        # for attr in dir(dbResponse):
        #     print(f"******{attr}*******")
        if dbResponse.deleted_count==1:
            return Response(response=json.dumps({"message":"user deleted","id":f"{id}"}),status=200,mimetype='application/json')
        
        return Response(response=json.dumps({"message":"nothing to delete"}),status=200, mimetype='application/json')
    except Exception as ex:
        print("*************")
        print(ex)
        print("***********")
        return Response(response=json.dumps({"message":"sorry can't delete user"}),status=500, mimetype='application/json')

############################################main----main----main-----########################################

if __name__=='__main__':
    app.run(port=80,debug=True)