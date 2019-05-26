# chatbot
Minimal chatbot using Django channels

# create python virtual env assuming python version >=3.0
python -m venv venv

# activate the env
source venv/bin/activate

pip install -r requirement.txt

# prepare DB
python3 manage.py makemigrations
python3 manage.py makemigrations intellibot

python3 manage.py migrate
python3 manage.py migrate intellibot

# To flush database changes and load static Questions data into DB
#python manage.py flush

python3 manage.py loaddata Questions.json

# Execute the server
http://127.0.0.1:8000/chat/lobby
~


