FROM python:3.7-slim

LABEL maintainer=""

ENV PYTHONDONTWRITEBYTECODE 1

#RUN mkdir cache

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# copy main code
#COPY ./imgproc /imgproc/
# run scripts to download assets from external sources
#RUN python /imgproc/download_models.py

COPY ./web /web/

WORKDIR /web
CMD gunicorn --bind 0.0.0.0:$PORT app:app