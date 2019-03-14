FROM python:3.5
COPY . /app 
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["scripts/app.py"]
