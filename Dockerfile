FROM python:3.9.6

RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 4000

CMD ["python", "manage.py", "runserver"]
