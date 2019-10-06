FROM ubuntu:latest

RUN apt-get   update
RUN apt-get  install  -y  python3
RUN  apt-get install -y python-pip
RUN pip install flask

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]