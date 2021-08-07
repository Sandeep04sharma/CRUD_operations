# ShoppingCart Rest Api

In this repository I'm explaining you, how to create a Shopping Cart using REST API in python with flask and mongoDB, and apply CRUD(Create, Read, Update and Delete) operations on a cart.

Demo: See it on youtube https://www.youtube.com/watch?v=9g-GxTwakXk

# Problem Statement

##### To create a shopping cart REST API(Use Python/Mongodb) that handles CRUD operations for a specific user like create cart, get items, add items and remove items.

## Steps to be follow:

* MongoDB : To create and maintain database
* Postman App : To make requests to API from client side
* Python(3.7) or (any python3 version): To create the API

### Download and Install Required tools
* MongoDB Community Version (5.0.1) : https://www.mongodb.com/try/download/community
* Postman : https://www.postman.com/downloads/
* Python (3.7) : https://www.python.org/downloads/

### Required packages for python
* flask : To work with flask framework in python
* pymongo : To work with MongoDB database from python
##### Command to install required packages
* All packages at once : pip install -r requirements.txt
* Individual packages : pip install <package_name>
* <package_name> : flask, pymongo
#### Operations that can be performed with API
* Create and/or Add items to cart
* Get items in cart
* Update price, quantity for item in cart
* Remove specific item from cart
* Empty cart
#### Explaination about different operations
##### Create and/or Add items to cart :
By performing this operation, if the collection/table doesn't exist in MongoDB, than it will create the collection and add item to the cart, else if the collection already exists, then it will add item to existig cart.
* EndPoint : localhost:5000/carts
* Methods : POST
* form_data : "name", "price", "quantity"
##### Get items in cart :
This operation allow you to get all the items present in the cart
* EndPoint : localhost:5000/carts
* Methods : GET
##### Update price/quantity of item in cart
* This operation allow you to update name of item present in the cart by providing item id.
* EndPoint : localhost:5000/carts/name/{item_id}
* Methods : PUT
* form_data : "price", "quantity"

##### Remove specific item from cart
* This operation allows you to remove specific item from cart by providing its item id.
* EndPoint : localhost:5000/carts/{item_id}
* Methods : DELETE
##### Empty Cart
* This operation allows you to empty your cart by removing all items in the cart.
* EndPoint : localhost:5000/carts
* Methods : DELETE
