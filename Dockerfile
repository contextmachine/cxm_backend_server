FROM python:3.9
WORKDIR /code
COPY . .
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
ENV AWS_DEFAULT_REGION=ru-central1 AWS_ACCESS_KEY_ID=YCAJEfPewAGyo2K-BtlmWNl58 AWS_SECRET_ACCESS_KEY=YCMA8ZF2s_YFoD1WvsMCaym8dx4ZR9eXJ6_f5mmL STORAGE=https://storage.yandexcloud.net/ BUCKET=lahta.contextmachine.online NAME=lahta
ENV HOST=0.0.0.0, PORT=8181
CMD ["python", "main.py"]
