# Use python3 image
FROM python:3-alpine

# Set working directory
WORKDIR /app

# Update apk
RUN apk update

# Install dependencies
RUN apk add --no-cache live-media-utils
RUN apk add --no-cache bash

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy jidocore files
COPY rtsparchiver/ /app/rtsparchiver/
COPY README.md /app/README.md
COPY main.py /app/main.py

# Set entrypoint
ENTRYPOINT ["python3", "main.py"]
