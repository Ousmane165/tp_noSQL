#!/bin/bash

# Définition des ports pour les shards et mongos
PORT1=27018
PORT2=27019
PORT3=27020

# Création des répertoires pour les fichiers de données
mkdir -p data/configdb data/shard1 data/shard2

# Démarrage des serveurs shard
mongod --port $PORT1 --dbpath data/shard1 --shardsvr --fork --logpath data/shard1/mongod.log
mongod --port $PORT2 --dbpath data/shard2 --shardsvr --fork --logpath data/shard2/mongod.log

# Démarrage du serveur de configuration
mongod --port 27017 --dbpath data/configdb --configsvr --fork --logpath data/configdb/mongod.log

# Démarrage de mongos
mongos --configdb localhost:27017 --port $PORT3 --fork --logpath data/mongos.log

# Pause pour permettre le démarrage des services
sleep 5

# Configuration du sharding via mongosh
mongosh --port $PORT3 --eval '
sh.addShard("localhost:'$PORT1'")
sh.addShard("localhost:'$PORT2'")
sh.enableSharding("sharding_db")
sh.shardCollection("sharding_db.realEstate", { _id: "hashed" })
'
