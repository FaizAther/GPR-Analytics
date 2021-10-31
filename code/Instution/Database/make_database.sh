#!/bin/sh

export PYTHONPATH=`pwd | sed 's/\/Instution\/Database$//'`
echo "export PYTHONPATH=$PYTHONPATH"
rm -rf gpr.db
sqlite3 gpr.db < creation.sql
sqlite3 gpr.db < populate.sql
sqlite3 gpr.db < events.sql
cp gpr.db ../
cp gpr.db ../../
rm -rf $PYTHONPATH/uploads
mkdir $PYTHONPATH/uploads
touch $PYTHONPATH/uploads/.hello_world
