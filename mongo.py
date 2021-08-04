import os, pymongo

if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        cnn = pymongo.MongoClient(url)
        print("mongo is connected")
        return cnn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to mongo: %s") % e


cnn = mongo_connect(MONGO_URI)
coll = cnn[DATABASE][COLLECTION]

documents = coll.find()
for doc in documents:
    print(doc)