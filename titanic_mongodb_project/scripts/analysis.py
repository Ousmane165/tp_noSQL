from db.mongo_connection import get_database

def run_analysis():
    db = get_database()
    col = db["Passengers"]
    print("Total passagers:", col.count_documents({}))
    print("Survécu:", col.count_documents({"Survived": 1}))
    print("Femmes:", col.count_documents({"Sex": "female"}))
    print("≥ 3 enfants:", col.count_documents({"Parch": {"$gte": 3}}))
