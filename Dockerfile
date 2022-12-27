# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /opt/app

# Install dependencies
COPY requirements.txt /code/

RUN pip install pillow

RUN pip install -r /code/requirements.txt

# Copy project
COPY . /opt/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
