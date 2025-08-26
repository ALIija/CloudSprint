# Multi-Service Container for Landing Page CMS
# Architecture: Wagtail + FastAPI + Celery + Nginx in one container
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=landing_page_cms.settings.production

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p /var/log/supervisor /var/log/nginx /var/log/celery

# Copy configuration files
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/celery.conf /app/celery.conf

# Collect static files
RUN python manage.py collectstatic --noinput

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app /var/log

# Switch to non-root user
USER appuser

# Expose port 80
EXPOSE 80

# Start supervisord (manages all services)
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
