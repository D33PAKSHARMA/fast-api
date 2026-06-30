from pymongo import MongoClient
import certifi

uri = DB_URL_from _env
client = MongoClient(uri,tls=True, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.test
