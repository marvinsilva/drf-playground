FROM python:3.7.5-slim-stretch

ENV PYTHONUNBUFFERED=1

WORKDIR /api

COPY . /api

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile --dev