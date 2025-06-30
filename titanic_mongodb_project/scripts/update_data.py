from db.mongo_connection import get_database

def update_embarked_and_rescued():
    db = get_database()
    col = db["Passengers"]
    col.update_many({"Embarked": {"$in": [None, ""]}}, {"$set": {"Embarked": "S"}})
    col.update_many({"Survived": 1}, {"$set": {"rescued": True}})
    print("Mise à jour des embarquements et 'rescued' faite.")

def increase_age():
    db = get_database()
    col = db["Passengers"]
    col.update_many({"Age": {"$ne": None}}, {"$inc": {"Age": 1}})
    print("Âge de tous les passagers augmenté de 1.")
