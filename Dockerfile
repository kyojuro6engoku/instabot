FROM python:3.10

WORKDIR /instabot

# Copy the requirements.txt file from the host to the /sakura directory in the Docker image
COPY requirements.txt /instabot/

# Run the pip install command to install the Python dependencies
RUN pip install -r requirements.txt

RUN python -m pip install pymongo

COPY ..

CMD ["python3", "insta.py"]
