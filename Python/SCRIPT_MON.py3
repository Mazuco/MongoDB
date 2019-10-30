#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#SCRIPT_MON.py3

"""
  Nesse script vamos
  rodar alguns scripts
  em python com o banco de 
  dados do MongoDB


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

db.fila.remove() # Apagar os dados escritos previamente
db.fila.insert({ "_id":1,"servico":"Intranet","status":0})
db.fila.insert({ "_id":2,"servico":"WebSite","status":0})
db.fila.insert({ "_id":3,"servico":"Backup","status":0})
db.fila.insert({ "_id":4,"servidor":"192.168.25.1","nome":"Asterisk"})
db.fila.insert({ "_id":5,"servidor":"192.168.25.2","nome":"FreeNas"})
db.fila.insert({ "_id":6,"servidor":"192.168.25.3","nome":"pfSense"})

for r in db.fila.find():
	print(r)



























