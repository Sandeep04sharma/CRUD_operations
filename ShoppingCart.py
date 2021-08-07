from flask import Flask, Response
import flask
from flask.globals import request
import pymongo
import json
from bson.objectid import ObjectId

# Connecting  with MongoDB database

try:
    mongo=pymongo.MongoClient(host='localhost',port=27017, serverSelectionTimeoutMS=1000)
    db=mongo.Miskaa
    mongo.server_info()
except:
    print("ERROR: can't connect to db")

app=Flask(__name__)


# creating shoping cart -------------

@app.route('/productCart',methods=['POST'])
def create_cart():
    try:
        item={'name':request.form["name"], 'price':request.form["price"],'quantity':request.form['quantity'] }
        dbResponse=db.productCart.insert_one(item)

        return Response(response=json.dumps({"message":"Item stored !", "id":f"{dbResponse.inserted_id}"}), status=200,mimetype='application/json')
    
    except Exception as ex:
        print(f"*******{ex}*********")

# retrieving/fetching items form cart

@app.route("/productCart",methods=["GET"])                          
def get_items_from_cart():
    try:
        data=list(db.productCart.find())                           
        for item in data:
            item["_id"]=str(item["_id"])
            
        return Response(response=json.dumps(data),status=500,mimetype='application/json')
    
    except Exception as ex:
        print(f"*******{ex}*********")
        return Response(response=json.dumps({"message":"Erro: cannot get items from cart !"}),status=500, mimetype='application/json' )


# update items in productCart

@app.route("/productCart/<id>",methods=["PATCH"])

def update_item(id):
    try:
        dbResponse=db.productCart.update_one({"_id":ObjectId(id)}, {"$set":{"price":request.form["price"],"quantity":request.form['quantity']}} )
        if dbResponse.modified_count==1:
            return Response(response=json.dumps({"message":"Item updated !"}), status=200,  mimetype='application/json')
        
        return Response(response=json.dumps({"message":"nothing to update !"}), status=200, mimetype='application/json')

    
    except Exception as ex:
        print(f"*******{ex}*********")
        return Response(response=json.dumps({"message":"Error: can't update item !"}),status=500,mimetype='application/json')



# delete item from products cart

@app.route("/productCart/<id>",methods=['DELETE'])

def delete_item(id):
    
    try:
        dbResponse=db.productCart.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count==1:
            return Response(response=json.dumps({"message":"Item deleted !","id":f"{id}"}),status=200,mimetype='application/json')
        
        return Response(response=json.dumps({"message":"Nothing to delete"}),status=200, mimetype='application/json')
    except Exception as ex:
        print(f"*******{ex}*********")
        return Response(response=json.dumps({"message":"Error: cannot delete item"}),status=500, mimetype='application/json')


# Empty cart, deleting all the items from product cart------

@app.route("/productCart", methods=["DELETE"])
def delete_cart():
    try:
        dbResponse = db.productCart.delete_many({})
        if (dbResponse.deleted_count > 0):
            return Response(
                response=json.dumps(
                    {"message":"All items Deleted !",
                    "count":f"{dbResponse.deleted_count}"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps(
                    {"message":"Cart is empty"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(f"*******{ex}*********")
        return Response(
            response=json.dumps({"message":"Error deleting items in cart"}),
            status=500,
            mimetype="application/json"
        )

# main function ---------------------

if __name__=='__main__':
    app.run(port=80,debug=True)
