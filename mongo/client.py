import pymongo

client = pymongo.MongoClient('mongodb+srv://anderson:<password>@cluster0-wbfjv.mongodb.net/test?retryWrites=true&w=majority')

database = client['streamers']

streams = database.streams