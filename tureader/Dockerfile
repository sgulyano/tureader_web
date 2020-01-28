FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY tureader/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000