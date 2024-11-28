# Use a slim Python image as the base
FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive
# Install necessary packages and clean up

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nginx \
    libmariadb-dev \
    libmariadb-dev-compat \
    default-libmysqlclient-dev \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*





# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and the Flask application
CMD ["sh", "-c", "service nginx start && python app.py"]