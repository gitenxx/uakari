FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app/admin
COPY admin/requirements.txt /app/admin/
RUN pip install -r requirements.txt
COPY . /app/