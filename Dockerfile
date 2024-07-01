FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt /code/

# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

# Start the Django development server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# # SOF https://stackoverflow.com/questions/55826941/run-pip-install-r-requirements-txt-not-working

# FROM python:3

# #set envionment variables
# ENV PYTHONUNBUFFERED 1

# # run this before copying requirements for cache efficiency
# RUN pip install --upgrade pip

# #set work directory early so remaining paths can be relative
# WORKDIR /ToDoApp

# # Adding requirements file to current directory
# # just this file first to cache the pip install step when code changes
# COPY requirements.txt .

# #install dependencies
# RUN pip install -r requirements.txt

# # copy code itself from context to image
# COPY . .

# # run from working directory, and separate args in the json syntax
# CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]


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
