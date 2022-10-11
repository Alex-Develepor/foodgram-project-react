FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt /
RUN pip install --upgrade pip
RUN apt update && apt install -y gcc libpq-dev
RUN pip install -r /requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]