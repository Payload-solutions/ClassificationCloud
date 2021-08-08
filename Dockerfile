FROM python:3.9.6

RUN pip install --upgrade pip

WORKDIR /db_service

ENV FLASK_APP main.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 4000

COPY . .

CMD ["flask", "run"]
