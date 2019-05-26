FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/.

RUN python manage.py migrate && python manage.py makemigrations intellibot && python manage.py migrate intellibot && python manage.py loaddata Question.json && python manage.py collectstatic --noinput
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]