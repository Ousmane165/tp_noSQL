from db.connection import classes

def average_final():
    print("\n📊 Moyenne des notes finales :")
    pipeline = [
        {"$match": {"className": "Mathematics 101"}},
        {"$unwind": "$students"},
        {"$group": {"_id": "$className", "avgFinal": {"$avg": "$students.grades.final"}}}
    ]
    for doc in classes.aggregate(pipeline):
        print(doc)

def max_final():
    print("\n📈 Note finale maximale :")
    pipeline = [
        {"$match": {"className": "Mathematics 101"}},
        {"$unwind": "$students"},
        {"$group": {"_id": "$className", "maxFinal": {"$max": "$students.grades.final"}}}
    ]
    for doc in classes.aggregate(pipeline):
        print(doc)