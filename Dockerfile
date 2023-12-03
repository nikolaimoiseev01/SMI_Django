FROM ubuntu:latest
LABEL authors="vita"

ENTRYPOINT ["top", "-b"]

FROM --platform=linux/amd64 python:3.11.6

RUN pip install "poetry==1.7.1"

COPY pyproject.toml /usr/src/app/

WORKDIR /usr/src/app

RUN poetry config virtualenvs.in-project true && poetry install --no-interaction --no-ansi

COPY . /usr/src/app

EXPOSE 5000

RUN poetry run python manage.py runserver 0.0.0.0:8888

# CMD ["poetry run", "python manage.py runserver 0.0.0.0:8888"]