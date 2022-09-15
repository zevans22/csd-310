<<<<<<< Updated upstream

=======
import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.i8dgnsj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collection = db["students"]
>>>>>>> Stashed changes
