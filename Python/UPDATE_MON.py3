#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#UPDATE_MON.py3

"""
  Nesse script vamos
  fazer algumas 
  atualizações 

  Modificado em 03 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

try:
	from pymongo import MongoClient
except:
    print("[!] Por favor, intale a biblioteca mongodb com o comando: sudo apt-get install python3-pymongo' ou 'pip3 install --upgrade pymongo'")


client = MongoClient('mongodb://admin:123456@localhost:27017')
db=client["devops"]

db.fila.update({"_id":2},{"$set":{"servico":"Linux"}})
db.fila.update({"_id":4},{"$set":{"servidor":"192.168.1.100"}}
)

for r in db.fila.find():
	print(r)
































