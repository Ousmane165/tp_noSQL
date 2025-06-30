from db.mongo_connection import get_database

def delete_unknown_age_not_survived():
    db = get_database()
    col = db["Passengers"]
    result = col.delete_many({"Survived": 0, "Age": {"$in": [None, ""]}})
    print(f"Supprimés (âge inconnu + non survivants) : {result.deleted_count}")

def delete_empty_ticket():
    db = get_database()
    col = db["Passengers"]
    result = col.delete_many({"$or": [{"Ticket": {"$exists": False}}, {"Ticket": ""}]})
    print(f"Supprimés (ticket vide) : {result.deleted_count}")
