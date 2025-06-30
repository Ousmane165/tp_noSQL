from db.connection import classes

def find_students_with_high_final():
    print("\n🎯 Étudiants avec final > 85 :")
    results = classes.find({"students.grades.final": {"$gt": 85}})
    for doc in results:
        print(doc)