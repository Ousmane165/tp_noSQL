from db.mongo_connection import get_database

def find_doctors():
    db = get_database()
    col = db["Passengers"]
    results = col.find({"Name": {"$regex": r"Dr\.", "$options": "i"}})
    for r in results:
        print(r.get("Name"))
