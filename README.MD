#python django postgresql

1.) create a virtual env, for dependency issues use python 3.7.1

python3 -m venv env_name

pip install -r requirements.txt #for virtual env reqirement

2.) for running services create a user, according to settings use credentials file for user and password... also create a database in postgresql...for simplicity use data_entry as database name...

3.)django \
python3 manage.py makemigrations\
python3 manage.py migrate\
python3 manage.py runserver


#maintaining frontEnd

## html files are located inside templates...
## 
