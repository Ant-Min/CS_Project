"""
Created on Sat Nov 20 15:59:14 2021

@author: 1957878_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ crud operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:39092' % 
                                  (username, password))
        self.database = self.client['project']
    
    def create(self, data):
        if data is not None:
            self.db.animals.insert(data) #data should be a dictionary
            print("Document inserted")
        else:
            raise Exception("Nothing to save because data parameter is empty")
    
    ''' read finds a specified object in the collection
        @param self is the database in question
        @param parameter is the object key
        @param specific is the object value '''
    def read(self):
        try:
            self.database.animals.find()
        except:
            raise Exception("Not a valid search")
            
    def update(self, parameter, original, specific):
        if self.database.animals.findOne({parameter: original}) is not None:
            self.database.animals.update({parameter: original}, {"$set": {parameter: specific}})
            self.database.animals.find({parameter: specific})
        else:
            raise Exception("Entry not found")
     
    def remove(self, parameter, specific):
        if self.database.animals.findOne({parameter: specific}) is not None:
            self.database.animals.remove({parameter: specific})
            self.database.animals.find({parameter: specific})
        else:
            raise Exception("Entry not found")  