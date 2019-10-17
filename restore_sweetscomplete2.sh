#!/bin/sh
mongorestore -d sweetscomplete2 -c customers ./dump/sweetscomplete2/customers.bson
mongorestore -d sweetscomplete2 -c products ./dump/sweetscomplete2/products.bson
mongorestore -d sweetscomplete2 -c purchases ./dump/sweetscomplete2/purchases.bson


