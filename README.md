
* Create private `.env` file inside of project directory. 
Copy all data from `.env_example` and paste inside of `.env` file. 
**Note**: Change the values of secrets to yours. 

* This project uses Postgresql, so, create Postgresql database:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib
sudo su - postgres
```
* Enter postgres console:
```
psql
CREATE DATABASE telegram;
CREATE USER telegramuser WITH PASSWORD 'pasword';
ALTER ROLE telegramuser SET client_encoding TO 'utf8';
ALTER ROLE telegramuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE telegramuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE telegram TO "telegramuser";
```


* Finally, run project with command: `python3 manage.py runserver`
* PROFIT!