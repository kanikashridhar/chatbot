# Intelli Bot
Minimal chatbot using Django

# How to Run

## Option1 - Using Docker
* cd localdir
```
cd chatbot
```
* Build the docker image
```
docker build -t chatbot:v1.0 .
``` 
* Run the docker image
```
docker run -p 8000:8000 chatbot:v1.0
```
This will start the server and you can find the bot by browsing to [http://localhost:8000/chat/ ](http://127.0.0.1:8000/chat/)

## Option 2 - Without Docker
* Install Python 3.x if not already
* Create virtual env
```
cd chatbot
python3 -m venv venv
```
* activate the env
```
source venv/bin/activate
```
* Now install the requirements
```
pip install -r requirements.txt
```
* prepare DB
```
python3 manage.py makemigrations
python3 manage.py makemigrations intellibot
python3 manage.py migrate
python3 manage.py migrate intellibot
```
* To load static Questions data into DB
```
python3 manage.py loaddata Question.json
```
* We disabled the DEBUG mode in settings s using whitenoise to serve the static files
```
python3 manage.py collectstatic
```

* Execute unit tests (if required)
```
python manage.py test intellibot/tests
```

* Run the server
```
python3 manage.py runserver
```
Now you can access the bot at [http://127.0.0.1:8000/chat/](http://127.0.0.1:8000/chat/)

# Inspiration
The codebase makes use of Django Channels and is based on the documentation [here](https://channels.readthedocs.io/en/latest/tutorial/part_2.html)

# Desired Improvements

Due to lack of time it was not feasible to integrate with a machine learning service like Azure's Bot Service or Amazon's Lex or any other Natural Language Processing (NLP) service which could help in finding intents and result in a much more effective bot. 
