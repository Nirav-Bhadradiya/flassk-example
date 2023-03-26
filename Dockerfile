# Build stage
FROM python:3.9-slim-buster AS build

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask API code into the container
COPY app.py .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run stage
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the installed Python dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the Flask API code from the build stage
COPY --from=build /app/app.py .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
