# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/instabot

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip

# Make start.sh executable
RUN chmod +x start.sh

# Run start.sh when the container launches
CMD ["./start.sh"]
