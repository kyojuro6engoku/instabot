# Use the official Python image as a parent image
FROM python:3.8-slim

# Create a working directory
WORKDIR /instabot

# Copy the Python script and requirements.txt into the container
COPY instagram_downloader_bot.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
# Copy the start.sh script into the container
COPY start.sh .

# Make the start.sh script executable
RUN chmod +x start.sh

# Run the start.sh script when the container starts
CMD ["./start.sh"]
