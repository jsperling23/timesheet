FROM python:slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY app/ app/
COPY .env .env

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.app:app"]
