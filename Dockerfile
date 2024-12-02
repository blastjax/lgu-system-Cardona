# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file from the host to the container
COPY ./requirements.txt ./requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code from the host to the container
COPY ./alembic /code/alembic
COPY ./app /code/app
COPY ./alembic.ini /code/.alembic.ini

# Secure the app to not run as root
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /code
RUN chown -R appuser /code/app
USER appuser

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]