from datetime import datetime
import pymongo

print('make connection...')
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

print('databases list...')
print(client.list_database_names())

print('choose db...')
DB_PROJ = "proj"
db = client[DB_PROJ]

print('look collections inside the db...')
print(db)
print(db.list_collection_names())

print('create new collection and see id of inserted item...')
res = db["demo"].insert_one({"foo":"bar"})
print(res, 'inserted id:', res.inserted_id)

COLLECTION_USERS = "users"

def user_factory(username: str, age: int) -> dict:
    res = {"username":username,
           "created_at":datetime.now(),
           "age": age,
           }
    return res

users_collection = db[COLLECTION_USERS]
admin_user = user_factory("admin", 20) # make a dict
admin_user["is_admin"] = True # add feature

print('insert in db')
res2 = users_collection.insert_one(admin_user)
print(res2, 'inserted id:', res2.inserted_id)


users = [user_factory("sam", 22), user_factory("john", 24)]
results = users_collection.insert_many(users)
print(results, results.inserted_ids)

user_admin = users_collection.find_one({ "username": "admin" })
print(user_admin, user_admin["_id"], user_admin["username"])

res = db["demo"].insert_one(
    {
        "user_admin": user_admin["_id"],
    }
)

print(res, res.inserted_id)

