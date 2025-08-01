# Use official Python slim image for smaller footprint
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY test-demo2/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY test-demo2/test.py .

# Command to run the transformation service
CMD ["python", "test.py"]