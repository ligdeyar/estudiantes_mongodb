import pymongo 
import os

class MongoDB:
           
    @staticmethod    
    def getDB(): 
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'

        ##Conecction String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format ( 
            user,
            password,
            cluster, 
            query_string )

        client = pymongo.MongoClient(uri)
        ##conection with BD
        db = client[os.environ['DB']]
      

        return client, db
    