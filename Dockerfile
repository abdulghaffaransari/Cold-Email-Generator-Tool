# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container's /app directory
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application runs on (if applicable, e.g., 8080)
EXPOSE 8080

# Run the application
CMD ["python3", "app/main.py"]
