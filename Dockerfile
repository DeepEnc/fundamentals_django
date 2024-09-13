FROM python:latest

WORKDIR /app

COPY requirements.txt /app/
COPY fundamentals_django /app/fundamentals_django/

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

# Set working directory to the Django project
WORKDIR /app/fundamentals_django

# Ensure database migrations are applied at runtime, not during build
ENTRYPOINT ["python3", "manage.py"]

# Run the development server
CMD ["runserver", "0.0.0.0:8000"]
