FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /taskapp
WORKDIR /taskapp
COPY requirements.txt /taskapp/
RUN pip install -r requirements.txt
COPY . /taskapp/