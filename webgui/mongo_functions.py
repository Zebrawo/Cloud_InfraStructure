from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

# Connect to MongoDB
client = MongoClient()
db = client.cli
mongo_users = db.users
mongo_records = db.Arecords

# Functie voor het opslaan van de gebruiker in MongoDB
def add_user(name, email, token):
    user = mongo_users.find_one({'email': email})
    if user:
        print("User already excists")
        return user['_id']
    else:
        user = {
            'name': name,
            'email': email,
            'token': token,
            'codes': []
        }
        result = mongo_users.insert_one(user)
        print(f"Customer with ID {result.inserted_id} created.")
        return result.inserted_id

#Functie voor het opslaan van wanneer een Record is aangepast
def time_change_FQDN(fqdn, ipv4,email):
    # Het controleren van of de FQDN al bestaat in de DB
    record = mongo_records.find_one({"fqdn": fqdn})
    if record:
        # Als de record bestaat. Controlleer of de IP address is aangepast
        if record["ipv4"] != ipv4:
            # Als de ip address is aangepast. Dan passen we dat aan in MongoDB met de nieuwe IP & Timestamp
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            result = mongo_records.update_one({"fqdn": fqdn}, {"$set": {"ipv4": ipv4, "timestamp": dt_string, "action": "changed"}})
            print(f"Record with FQDN {fqdn} updated. New IP address: {ipv4}")
        else:
            # Als het al bestaat met de juiste rechten doe niks
            print(f"Record with FQDN {fqdn} already exists.")
    else:
        # Als de record niet bestaat voeg dan toe aan de MongoDB
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        record = {
            "fqdn": fqdn,
            "ipv4": ipv4,
            "email": email,
            "action": "created",
            "timestamp": dt_string
        }
        result = mongo_records.insert_one(record)
        print(f"Record with FQDN {fqdn} and IP address {ipv4} created.")

        return result.inserted_id
    
def change_action_delete(fqdn, email):
    # Zoek het document met de gegeven FQDN
    record = mongo_records.find_one({"fqdn": fqdn})
    if record:
        # Update het document met de nieuwe actie en timestamp
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        result = mongo_records.update_one({"fqdn": fqdn}, {"$set": {"timestamp": dt_string, "action": "deleted", "email": email}})
        print(f"Record with FQDN {fqdn} updated with action deleted and timestamp {dt_string}.")
        return result
    else:
        print(f"No record found with FQDN {fqdn}.")
