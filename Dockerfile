FROM python:3

WORKDIR /database

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY /Database .

CMD [ "python3", "database.py"]