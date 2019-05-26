# chatbot
Minimal chatbot using Django channels

# create python virtual env assuming python version >=3.0
python -m venv venv

# activate the env
source venv/bin/activate

pip install -r requirement.txt

# prepare DB
python manage.py makemigrations intellibot

python manage.py migrate intellibot

# To flush database changes and load static Questions data into DB
python manage.py flush

python manage.py loaddata Questions.json
~


