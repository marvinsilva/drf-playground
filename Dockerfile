FROM python:3.7.5-slim-stretch

WORKDIR /app

COPY . /app

# installs non-dev dependencies to system's python from pipfile.lock
RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile