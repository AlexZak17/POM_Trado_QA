import pymongo
from urllib.parse import quote
from bson import ObjectId

password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"
ID_alex = '641af6d2b9ef3304a16725de'


def create_mongo_connection(user_name, encoded_password, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db


def get_specific_key_value(db, collection_name, document_id, key):
    collection = db[collection_name]
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        value = document.get(key)
        return value
    else:
        return None


def alex_SMS_code():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    code_numbers = get_specific_key_value(db, "users", ID_alex, "loginCode")
    return code_numbers
