FROM python:3.14-slim

WORKDIR /app/app

COPY . /app

RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]