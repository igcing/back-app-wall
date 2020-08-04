import pymongo

class MongoDB:
    URL = "mongodb://productListUser:productListPassword@mongo:27017/admin"
    def __init__(self):
        pass
    def _getConnection(self,url):
        try:
            print(url)
            client = pymongo.MongoClient(url)
            print(client)
            return client
        except Exception as error:
            print("Error connecting mongodb - {}".format( error ))
    
    def _getDB(self,client):
        try:
             return client["promotions"] # name database  
        except Exception as error:
            print("Error connecting mongodb - {}".format( error ))
    
    def _getCollection(self,db):
        try:
            return db["products"] # name collections
        except Exception as error:
            print("Error connecting mongodb - {}".format( error ))
    
    def getProducts(self):
        try:
            return self._getCollection(self._getDB(self._getConnection(self.URL)))
        except Exception as error:
            print("Error connecting mongodb - {}".format( error ))