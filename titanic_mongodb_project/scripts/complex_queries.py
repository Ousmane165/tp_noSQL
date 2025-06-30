from db.mongo_connection import get_database

def youngest_passengers():
    db = get_database()
    col = db["Passengers"]
    results = col.find({"Age": {"$ne": None}}).sort("Age", 1).limit(10)
    for r in results:
        print(r.get("Name"), "-", r.get("Age"))

def second_class_not_survived():
    db = get_database()
    col = db["Passengers"]
    results = col.find({"Survived": 0, "Pclass": 2})
    for r in results:
        print(r.get("Name"))
