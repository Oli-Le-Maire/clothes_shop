# clothes_shop
# to be completed


## SETUP A DATABASE
In the Command Line:

Install the Psycopg Module
```bash
pip install psycopg2-binary
```

Go into PostgreSQL
```bash
psql
```

CREATE DATABASE stock;

create a database.ini file and insert the parameters required to help make a connection

create a .gitignore file and put database.ini in there so that Github does show sensitive information such as passwords etc

create a config.py file so that connection parameters can be created from the contents of the database.ini file

create a connect.py file

python connect.py
to connect to the stock database, and create a table called current_stock (unless one is already created))



BUG & BUG RESOLUTION
when typing in - python connect.py, this was returned:
Connecting to the PostgreSQL database...
FATAL:  role "postgres" does not exist

to fix this, this was typed into the command line:
created a connect.py file to connect to the database
then this shows up:
Shall the new role be a superuser? (y/n)
type y


createuser postgres --interactive

PROGRESS:
Currently going by the following tutorial: https://www.postgresqltutorial.com/postgresql-python/connect/
