FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt /code/

# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

# Start the Django development server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
