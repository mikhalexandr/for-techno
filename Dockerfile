FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-cache

COPY . .

RUN find . -type d -name "__pycache__" -exec rm -r {} +

CMD ["uvicorn", "cmd.server.main:app", "--host", "0.0.0.0", "--port", "5252"]
