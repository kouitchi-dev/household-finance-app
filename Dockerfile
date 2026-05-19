FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r /app/requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]