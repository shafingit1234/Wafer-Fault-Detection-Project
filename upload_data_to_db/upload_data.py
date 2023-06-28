import pandas as pd
# We dump data in the form of json hence we need json library.
import json
import certifi
import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://<username>:<password>@cluster0.m3lkv93.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
# database_name = "sensor"
DATABASE_NAME = "wafer_fault_project"
COLLECTION_NAME = "waferfault"
df = pd.read_csv(
    "D:\Projects\Wafer-Fault-Detection-Project\datasets\wafer_dataset.csv")
# convert data into json format
# df
df = df.drop("Unnamed: 0", axis=1)
json_record = list(json.loads(df.T.to_json()).values())

# Now dump the data into database.
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
