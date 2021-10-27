#!/bin/sh

rm -rf gpr.db
sqlite3 gpr.db < creation.sql
sqlite3 gpr.db < populate.sql
sqlite3 gpr.db < events.sql
cp gpr.db ../
