FROM jgbustos/ml-model-base:latest

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["scripts/app.py"]
