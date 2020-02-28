FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_19_6:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient_19_6:$PATH

RUN mkdir /code
WORKDIR /code

RUN mkdir /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip -P /opt/oracle \
&& unzip /opt/oracle/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip -d /opt/oracle

RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-sdk-linux.x64-19.6.0.0.0dbru.zip -P /opt/oracle \
&& unzip /opt/oracle/instantclient-sdk-linux.x64-19.6.0.0.0dbru.zip -d /opt/oracle

RUN apt-get update \
&& apt-get install libaio1

RUN echo sh -c "/opt/oracle/instantclient_19_6 > /etc/ld.so.conf.d/oracle-instantclient" \
&& ldconfig


COPY tureader/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

ENTRYPOINT ["/code/tureader/run.sh"]