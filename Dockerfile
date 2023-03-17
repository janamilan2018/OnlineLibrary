FROM ubuntu
MAINTAINER milan
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update
WORKDIR /app
COPY Onlinelibrary /app/Onlinelibrary
COPY requirements.txt /app/requirements.txt
RUN apt-get -y install python3 python3-pip
RUN pip install -r /app/requirements.txt
EXPOSE 8000
CMD ["python3","Onlinelibrary/manage.py","runserver","0.0.0.0:8000","--insecure"]
