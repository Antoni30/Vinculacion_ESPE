from pymongo.mongo_client import MongoClient
import json
from ..models.Internal import Internal

uri = "mongodb+srv://registroespedb:Jpb3GO9zl7fQTlsu@cluster0.2lmju3k.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

user_toni = Internal(campus='matriz', 
         career='software',
         ci='1725205106',
         email='ttoapanta1@espe.edu.ec',
         id_espe='L00001',
         lastnames='Toapanta',
         names='Toni',
         type_espe='student'
        )

def add_user_db(user: Internal):
    db = client['sistema_registro_espe_db']
    collection = db['users']
    insert_result = collection.insert_one({
            "names": user.names,
            "lasnames": user.lastnames,
            "career": user.career,
            "campus": user.campus,
            "ci": user.ci,
            "email": user.email,
            "id_espe": user.id,
            "type_espe": user.type
    })
    client.close()
    return insert_result.inserted_id
id_resultante = add_user_db(user_toni)
print("Documento insertado con ID: ", id_resultante)