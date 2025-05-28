FROM python:3.10-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
COPY app.py .
COPY classes.txt .
COPY models/best.pt models/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the API server
CMD ["python", "app.py"]
