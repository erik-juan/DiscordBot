FROM python:3.7.12-buster

COPY requirements.txt requirements.txt
COPY bot.py bot.py
COPY spotifyFunction.py spotifyFunction.py

RUN ["python3", "-m", "pip", "install", "-r", "requirements.txt"]

CMD python bot.py 1>>logs.txt 2>>logs.txt