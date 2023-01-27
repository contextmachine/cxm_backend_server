
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . .
VOLUME ["/code/share"]
ENV HOST=0.0.0.0, PORT=8181

CMD ["python", "main.py"]
