FROM python:3.11-slim

WORKDIR /app

COPY main.py /app/

COPY data /app/data

RUN mkdir -p log

RUN chmod +x /app/main.py


CMD ["python", "/app/main.py"]