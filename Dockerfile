# Base image with Python
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install system dependencies (e.g., OpenCV dependencies)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the FastAPI app port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "$PORT"]

