from pymongo import MongoClient
import pandas as pd

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["PokemonDB"]
collection = db["Pokemons"]

# --- Exercice 1 : Création de la base et collection ---
print("Base 'PokemonDB' et collection 'Pokemons' créées.")

# --- Exercice 2 : Insertion des données ---
df = pd.read_csv("pokemonGO.csv")
data = df.to_dict(orient="records")
collection.insert_many(data)
print("Données insérées dans la collection.")

# --- Exercice 3 : Lecture des données ---
print("\n--- Pokémons de type 'Feu' ---")
fire_pokemons = collection.find({"Type 1": "Fire"})
for pokemon in fire_pokemons:
    print(pokemon)

print("\n--- Informations de Pikachu ---")
pikachu = collection.find_one({"Name": "Pikachu"})
print(pikachu)

# --- Exercice 4 : Mise à jour de Pikachu ---
collection.update_one({"Name": "Pikachu"}, {"$set": {"CP": 900}})
print("\nPikachu mis à jour (CP = 900)")

# --- Exercice 5 : Suppression de Bulbasaur ---
collection.delete_one({"Name": "Bulbasaur"})
print("\nBulbasaur supprimé.")
