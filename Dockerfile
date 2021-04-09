FROM python:3.8-slim-buster

WORKDIR /app

# install requirements
COPY ./app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy app files
COPY ./app .

# export run file
ENV FLASK_APP=/app/__init__.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]