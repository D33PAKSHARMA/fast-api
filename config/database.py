from pymongo import MongoClient
import certifi

uri = "mongodb+srv://Deepak:d33p1ks7899@cluster0.gpgm7th.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri,tls=True, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.test
