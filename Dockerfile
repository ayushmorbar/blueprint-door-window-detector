FROM python:3.10-slim

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
