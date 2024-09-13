FROM python:latest

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && pip install --upgrade pip && pip install -r requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

COPY fundamentals_django /app/fundamentals_django/

# Set working directory to the Django project
WORKDIR /app/fundamentals_django

# Ensure database migrations are applied at runtime, not during build
ENTRYPOINT ["python3", "manage.py"]

# Run the development server
CMD ["runserver", "0.0.0.0:8000"]
