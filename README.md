The purpose of this code is to demo how to extract data from a Mongo nested sub-documents in a normalized form.

# Instructions
1. Update config.ini with your MongoDB details including credentials.
2. Update name of the MongoDB collection (collection_name) in the extract.py or externelize in config file and read from there.
3. Input file contains the newline delimited profile IDs for which details (including user attributes) are to be extracted.

Sample document in MongoDB is as follows:
```
{
  "_id": {
    "$oid": "65475683de6beac1f7265575"
  },
  "profile_id": "ABCDCA12345",
  "client": {
    "client_attr1": "clientValue1",
    "identifier": "123456789"
  },
  "users": [
    {
      "GUID": "7a9e068a-b417-42ca-b359-ce106c69c0b1",
      "name": "Name11",
      "login_id": "abc1@email.com"
    },
    {
      "GUID": "a3e380b1-674a-4747-8992-9e39ce811e48",
      "name": "Name12",
      "login_id": "xyz1@email.com"
    }
  ]
}
```

Sample output with few profile level and few user level attributes will be as follows:

| GUID | login_id | profile_id | client.identifier |
| :---: | :---: | :---: | :---: |
| 7a9e068a-b417-42ca-b359-ce106c69c0b1 | abc1@email.com | ABCDCA12345 | 123456789 |
| a3e380b1-674a-4747-8992-9e39ce811e48 | xyz1@email.com | ABCDCA12345 | 123456789 |
| c474f04e-15c4-4987-9412-50ffef3140b3 | abc3@email.com | ABCDCA34567 | 345678901 |

Update the .py file as needed to include/exclude any additional attributes.