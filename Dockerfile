FROM python:3.7

WORKDIR /home/chatbot

COPY requirements.txt requirements.txt

#RUN apk add --no-cache --virtual .build-deps \
#    ca-certificates gcc postgresql-dev linux-headers musl-dev \
#    libffi-dev jpeg-dev zlib-dev

#With the below command, I'm asking Python to run the venv package, which creates a virtual environment named venv. The first venv in the command is the name of the Python virtual environment package, and the second is the virtual environment name that I'm going to use for this particular environment. When we created the project through PyCharm, Pycharm itself created the virtual env. But if we are working on the command prompt then we have to create the virtual env manually.
#RUN python -m venv venv
RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

RUN python3 manage.py makemigrations intellibot
RUN python3 manage.py migrate intellibot

RUN python3 manage.py loaddata Question.json
#COPY boot.sh ./
EXPOSE 8000

CMD ["python3 manage.py runserver"]
