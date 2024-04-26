FROM python:3.10-alpine

WORKDIR /code

RUN apk add --no-cache gcc musl-dev linux-headers python3

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD  python3 ./manage.py migrate && python3 ./manage.py runserver 0.0.0.0:8000