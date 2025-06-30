# TP : Utilisation de Mongo Shell (mongosh)

Ce TP a pour objectif de vous faire manipuler les commandes de base de `mongosh`, le shell interactif de MongoDB.

---

## 🧪 Partie 1 : Exploration des Bases de Données et Collections

```shell
# 1. Connexion
mongosh

# 2. Lister les bases de données
show dbs

# 3. Sélectionner une base (ou la créer)
use testDB

# 4. Créer une collection
db.createCollection("testCollection")

# 5. Afficher les collections
show collections
```

---

## ✍️ Partie 2 : Manipulation des Données

```shell
# 6. Insérer un document
db.testCollection.insertOne({name: "test", value: 1})

# 7. Lire tous les documents
db.testCollection.find()

# 8. Mettre à jour un document
db.testCollection.updateOne({name: "test"}, {$inc: {value: 1}})

# 9. Lire à nouveau pour vérifier la mise à jour
db.testCollection.find()

# 10. Supprimer le document
db.testCollection.deleteOne({name: "test"})
```

---

## 🧹 Partie 3 : Nettoyage

```shell
# 11. Supprimer la collection
db.testCollection.drop()

# 12. Supprimer la base de données (en s'assurant d'être dans testDB)
use testDB
db.dropDatabase()
```

---

## ✅ Validation à chaque étape

- `show dbs` → pour voir les bases
- `show collections` → pour voir les collections
- `db.testCollection.find()` → pour voir les documents
