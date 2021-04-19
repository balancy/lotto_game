FROM python:3.9

RUN mkdir -p /usr/src/lotto/
WORKDIR /usr/src/lotto/

COPY . /usr/src/lotto/

CMD python main.py
