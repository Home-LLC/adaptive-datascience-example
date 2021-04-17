# pull official base image
FROM python:3.8.3

# set work directory
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get -y update \
    && apt-get install  -y gcc python3-dev musl-dev
    
# install dependencies
RUN pip install --upgrade pip
ADD . .
RUN pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["sh", "-c", "python s3.py"]