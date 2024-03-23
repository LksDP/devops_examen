# Usa una imagen base de Python
FROM python:3.9-slim as python_base

WORKDIR /app

COPY ./app .

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]