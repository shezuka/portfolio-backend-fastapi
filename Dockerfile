FROM python:3.12-alpine

WORKDIR /app
COPY . .

RUN pip install poetry
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "portfolio_backend_fastapi.main:app", "--host=0.0.0.0", "--port=8000"]