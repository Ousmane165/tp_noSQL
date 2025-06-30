from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["PokemonDB"]
collection = db["Pokemons"]


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        name = request.form.get("name")
        type_ = request.form.get("type")

        query = {}
        if name:
            query["Name"] = {"$regex": name, "$options": "i"}
        if type_:
            query["Type 1"] = type_

        results = list(collection.find(query))

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
