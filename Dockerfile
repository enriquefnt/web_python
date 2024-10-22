FROM python:3.9-slim-buster

# WORKDIR /app
WORKDIR /WEB_PYTHON
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]