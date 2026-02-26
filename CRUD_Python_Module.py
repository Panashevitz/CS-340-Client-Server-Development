from pymongo import MongoClient 
from bson.objectid import ObjectId

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, host, port, database, collection): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client[DB] 
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
            
    # Create Method to insert data
    def create(self, data):
        if data is not None: 
            insert_result = self.collection.insert_one(data)  # data should be dictionary
            return insert_result.acknowledged
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Read method to view data
    def read(self, query):
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print(f"Nothing to read, because no list was found: {e}")
            return []
    
    # Update method to modify the data
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            result = self.collection.update_many(query, {"$set": new_data})
            return result.modified_count
        else:
            raise Exception("Query and new_data parameters are required")
    
    # Delete method to remove data
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query parameter is empty")