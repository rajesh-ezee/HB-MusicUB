FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install build and runtime dependencies for OpenCV, PyTgCalls, and other packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
        libgl1 \
        libglib2.0-0 \
        build-essential \
        python3-dev \
        libffi-dev \
        libnacl-dev \
        libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy files and install requirements
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -U -r requirements.txt

# Default command
CMD ["bash", "start.sh"]
