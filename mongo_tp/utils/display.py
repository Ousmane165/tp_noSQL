from db.connection import classes

def show_all_documents():
    print("\n📚 Document final :")
    for doc in classes.find():
        print(doc)