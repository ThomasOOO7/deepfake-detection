FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    git \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Optional: Pre-download whisper model for faster startup
RUN python -c "import whisper; whisper.load_model('tiny', download_root='/app/models/whisper-tiny')"

# Expose Flask default port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
