# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy service and application files
COPY service/ ./service/
COPY setup.cfg .

# Create a non-root user and set permissions
RUN useradd --create-home --shell /bin/bash theia && \
    chown -R theia:theia /app

# Switch to the non-root user
USER theia

# Expose port
EXPOSE 8080

# Run the service with Gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
