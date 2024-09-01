# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY heartbeat.py .

# Install the required Python packages
RUN pip install requests

# Command to run the script
CMD ["python", "heartbeat.py"]
