FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install system deps for ffmpeg, opencv, pytgcalls, pycairo, etc.
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
        libopus-dev \
        libavformat-dev \
        libavutil-dev \
        libswresample-dev \
        libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

# istall kurigram
RUN mkdir /kurigram && pip install --no-cache-dir git+https://github.com/Itz-fork/Kurigram.git --target /kurigram

# Upgrade pip, setuptools, and wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -U -r requirements.txt

CMD ["bash", "start.sh"]
