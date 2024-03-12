import pymongo
import certifi





con_str = "mongodb+srv://KoryDevs:Austin19@atlascluster.lavai0l.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

client = pymongo.MongoClient(con_str,tlsCAfile=certifi.where())
db = client.get_database("KoryDevstest")