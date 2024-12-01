# Dockerfile
FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libyaml-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements files
COPY requirements/ requirements/

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements/production.txt \
    && rm -rf requirements

# Copy the application code
COPY . .

CMD ["python", "bot.py"]
