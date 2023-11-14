from pymongo import MongoClient
import pandas as pd
from pandas import json_normalize
import configparser

config=configparser.ConfigParser()
config.read('config.ini')

# MongoDB connection details
host = config.get('MongoDB', 'hostname')
port = int(config.get('MongoDB', 'port'))
database = config.get('MongoDB', 'database')
username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')

#read profile ID list from the input file
profile_list=open("Id_input.txt", 'r').read().split('\n')

# Connect to MongoDB
client=MongoClient(host, port, username=username, password=password)
db=client[database]
data=db.collection_name

result=data.find({"profile_id":{"$in": profile_list}},{"_id":0,"profile_id":1, "client.identifier":1, "users.GUID":1, "users.login_id":1})
intermediate_data=list(result)
df=pd.DataFrame(json_normalize(intermediate_data, "users", ["profile_id", ["client", "identifier"]]))
df.to_csv('output.csv', index=False)
