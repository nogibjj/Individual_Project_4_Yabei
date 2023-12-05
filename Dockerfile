FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "main:app", "--config", "gunicorn_config.py"]
