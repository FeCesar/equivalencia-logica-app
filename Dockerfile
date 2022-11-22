FROM python:3.9.4-slim-buster

WORKDIR /app

COPY static/ /app/static/
COPY templates/ /app/templates/
COPY .env /app/
COPY expressions.py /app/
COPY main.py /app/
COPY table.py /app/
COPY requirements.txt /app/

EXPOSE 5000

RUN python -m pip install --upgrade pip

RUN apt-get update \
&& apt-get -y install g++ libpq-dev gcc unixodbc unixodbc-dev

RUN apt-get -y install chromium-driver 

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]