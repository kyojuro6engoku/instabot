# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /instabot

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Upgrade pip (Add this step to upgrade pip)
RUN pip install --upgrade pip

RUN pip install pyrogram

# Copy your bot's source code into the container
COPY . .

# Start the bot when the container runs
CMD ["python3", "insta.py"]
