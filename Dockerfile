FROM python:3.8.5 
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app/admin
COPY admin/requirements.txt /app/admin/
RUN  /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/