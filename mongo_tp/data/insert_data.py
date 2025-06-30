from db.connection import classes

def insert_initial_class():
    classes.drop()  # Réinitialise
    classes.insert_one({
        "className": "Mathematics 101",
        "professor": "John Doe",
        "students": [
            {"name": "Charlie", "age": 21, "grades": {"midterm": 79, "final": 92}},
            {"name": "Dylan", "age": 23, "grades": {"midterm": 79, "final": 87}}
        ]
    })
    print("✅ Classe insérée.")