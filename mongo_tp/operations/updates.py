from db.connection import classes

def add_bob_and_update():
    classes.update_one(
        {"className": "Mathematics 101"},
        {"$push": {
            "students": {
                "name": "Bob",
                "age": 22,
                "grades": {"midterm": 75, "final": 85}
            }
        }}
    )
    classes.update_one(
        {"className": "Mathematics 101", "students.name": "Bob"},
        {"$inc": {"students.$.grades.final": 5}}
    )
    print("✅ Bob ajouté et mis à jour.")

def add_charlie_and_remove_alice():
    classes.update_one(
        {"className": "Mathematics 101"},
        {"$push": {
            "students": {
                "name": "Charlie",
                "age": 23,
                "grades": {"midterm": 82, "final": 88}
            }
        }}
    )
    classes.update_one(
        {"className": "Mathematics 101"},
        {"$pull": {"students": {"name": "Alice"}}}
    )
    print("✅ Charlie ajouté, Alice supprimée.")