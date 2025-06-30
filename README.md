# TP MongoDB – Réplication et Sharding en Local

## 📌 Objectif
Mettre en place un cluster MongoDB en local avec :
- Un **replica set** composé de 3 nœuds (1 primaire, 2 secondaires)
- Un **cluster sharding** avec 2 shards, 1 config server, et un mongos

---

## 🧪 Partie 1 : Réplication

### 📁 Fichiers :
- `replication_script.sh` : script pour lancer les 3 instances de MongoDB et initialiser le replica set
- `mongod.conf` : configuration MongoDB avec le nom du replica set

### ▶️ Lancement :
```bash
bash replication_script.sh
```

### 🧪 Test :
- Connectez-vous à une instance via `mongosh --port 27017`
- Vérifiez le status avec : `rs.status()`
- Ajoutez une base `GameOfThrones` et une collection `characters`
- Vérifiez que les données sont bien répliquées sur les ports `27018` et `27019`

---

## 🧩 Partie 2 : Sharding

### 📁 Fichiers :
- `sharding_script.sh` : script pour démarrer les shards, le config server et mongos
- `mongod_shard.conf` : configuration pour les shards (à adapter si utilisé manuellement)
- `mongod_config.conf` : configuration du config server
- `data/real_estate_sample.csv` : données à importer

### ▶️ Lancement :
```bash
bash sharding_script.sh
```

### 🧪 Test :
- Connectez-vous à mongos : `mongosh --port 27020`
- Vérifiez la configuration avec : `sh.status()`
- Importez le fichier CSV :
```bash
mongoimport --port 27020 --db sharding_db --collection realEstate --type csv --headerline --file data/real_estate_sample.csv
```
- Vérifiez la répartition :
```js
db.realEstate.getShardDistribution()
db.realEstate.find().explain("executionStats")
```

---

## 🧼 Nettoyage :
Pour arrêter les processus, utilisez :
```bash
ps aux | grep mongod
kill <pid>
```
ou
```bash
mongosh --port <PORT> --eval 'db.adminCommand({ shutdown: 1 })'
```

---

## 👨‍💻 Auteur
TP automatisé avec des scripts bash. À exécuter sur un environnement Linux avec MongoDB installé.

