FROM ubuntu:16.04
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]