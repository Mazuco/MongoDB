#!/bin/sh
mongorestore -d mongo_book -c books ./dump/mongo_book/books.bson
mongorestore -d mongo_book -c bookOrders ./dump/mongo_book/bookOrders.bson
mongorestore -d mongo_book -c Address ./dump/mongo_book/Address.bson
mongorestore -d mongo_book -c Person ./dump/mongo_book/Person.bson
mongorestore -d mongo_book -c transactions ./dump/mongo_book/transactions.bson
mongorestore -d mongo_book -c types ./dump/mongo_book/types.bson
mongorestore -d mongo_book -c blocks ./dump/mongo_book/blocks.bson
mongorestore -d mongo_book -c scam_details ./dump/mongo_book/scam_details.bson
mongorestore -d mongo_book -c scam_ico_documents ./dump/mongo_book/scam_ico_documents.bson
mongorestore -d mongo_book -c scam_ico_documents_extended ./dump/mongo_book/scam_ico_documents_extended.bson

