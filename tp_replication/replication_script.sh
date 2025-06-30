#!/bin/bash

# Définition des ports pour chaque instance MongoDB
PORT1=27017
PORT2=27018
PORT3=27019

# Création des répertoires pour les fichiers de données
mkdir -p data/db1 data/db2 data/db3

# Démarrage des instances mongod avec réplication activée
mongod --port $PORT1 --dbpath data/db1 --replSet rs0 --bind_ip localhost --fork --logpath data/db1/mongod.log
mongod --port $PORT2 --dbpath data/db2 --replSet rs0 --bind_ip localhost --fork --logpath data/db2/mongod.log
mongod --port $PORT3 --dbpath data/db3 --replSet rs0 --bind_ip localhost --fork --logpath data/db3/mongod.log

# Pause pour permettre le démarrage des instances
sleep 5

# Initialisation du replica set via mongosh
mongosh --port $PORT1 --eval '
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "localhost:'$PORT1'" },
    { _id: 1, host: "localhost:'$PORT2'" },
    { _id: 2, host: "localhost:'$PORT3'" }
  ]
})'
