FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

# Start the Django development server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# # Tuto https://hackernoon.com/fr/comment-dockeriser-et-d%C3%A9ployer-des-applications-Django 
# FROM python:3.9 

# #Install Django and other required packages 
# RUN pip install django 

# # Copy the Django project files into the image 
# COPY . /app 

# # Set the working directory 
# WORKDIR /app 

# # Start the Django development server 
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
