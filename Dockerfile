FROM python:3.10.7-slim

WORKDIR /app

COPY . .

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --only main --no-root

RUN poetry show

CMD ["poetry", "run", "gunicorn", "core.wsgi:application", "--bind", "0:8080"]
