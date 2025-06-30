import csv
from db.mongo_connection import get_database

def import_csv():
    db = get_database()
    collection = db["Passengers"]
    collection.delete_many({})  # Nettoyage

    with open("data/titanic.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        docs = []
        for doc in reader:
            for key in ['Age', 'SibSp', 'Parch', 'Fare', 'Survived', 'Pclass']:
                if key in doc and doc[key]:
                    try:
                        doc[key] = float(doc[key]) if '.' in doc[key] else int(doc[key])
                    except:
                        doc[key] = None
            docs.append(doc)
        if docs:
            collection.insert_many(docs)
    print("Importation terminée.")
