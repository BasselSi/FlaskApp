# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py /app/

# Install Flask
RUN pip install Flask

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

