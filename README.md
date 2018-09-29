please make sure you have installed python and pip <br/>
run the following commands line below:
# install requirement modules
pip install requirements.txt

# create initial db.SQLite3
python manage.py makemigrations
python manage.py migrate

# load initial data
python manage.py loaddata topics.json
python manage.py loaddata news.json

# run server (you can open it in local browser https://localhost:8000)
python manage.py runserver

# run testing API
python manage.py test
