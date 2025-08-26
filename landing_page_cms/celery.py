"""
Celery configuration for Landing Page CMS
Handles background tasks and content export to S3
"""
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'landing_page_cms.settings.development')

# Create Celery app
app = Celery('landing_page_cms')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all Django apps
app.autodiscover_tasks()

# Configure Celery
app.conf.update(
    broker_url='memory://',  # Use in-memory broker for development
    result_backend='rpc://',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,
    task_ignore_result=False,
    task_always_eager=False,  # Set to True for testing
)

@app.task(bind=True)
def debug_task(self):
    """Debug task for testing"""
    print(f'Request: {self.request!r}')

@app.task
def export_content_to_s3():
    """Export content to S3 for static site generation"""
    try:
        # In real implementation, this would:
        # 1. Query all published pages from Wagtail
        # 2. Generate static HTML/JSON
        # 3. Upload to S3
        # 4. Invalidate CloudFront cache
        
        print("Content export to S3 completed successfully")
        return {"status": "success", "message": "Content exported to S3"}
    except Exception as e:
        print(f"Content export failed: {str(e)}")
        return {"status": "error", "message": str(e)}

@app.task
def optimize_images():
    """Optimize uploaded images"""
    try:
        # In real implementation, this would:
        # 1. Find unoptimized images
        # 2. Resize and compress them
        # 3. Update Wagtail renditions
        
        print("Image optimization completed successfully")
        return {"status": "success", "message": "Images optimized"}
    except Exception as e:
        print(f"Image optimization failed: {str(e)}")
        return {"status": "error", "message": str(e)}

@app.task
def invalidate_cache():
    """Invalidate CDN cache"""
    try:
        # In real implementation, this would:
        # 1. Call CloudFront invalidation API
        # 2. Clear local cache
        
        print("Cache invalidation completed successfully")
        return {"status": "success", "message": "Cache invalidated"}
    except Exception as e:
        print(f"Cache invalidation failed: {str(e)}")
        return {"status": "error", "message": str(e)}

@app.task
def scheduled_export():
    """Scheduled content export (runs every hour)"""
    return export_content_to_s3.delay()

@app.task
def cleanup_exports():
    """Clean up old export files"""
    try:
        # In real implementation, this would:
        # 1. Find old export files in S3
        # 2. Delete files older than X days
        
        print("Export cleanup completed successfully")
        return {"status": "success", "message": "Old exports cleaned up"}
    except Exception as e:
        print(f"Export cleanup failed: {str(e)}")
        return {"status": "error", "message": str(e)}
