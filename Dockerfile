FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Set work directory
WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -U -r requirements.txt

# Default command
CMD ["bash", "start.sh"]
