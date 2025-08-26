# 🚀 Landing Page CMS - Wagtail + AWS Architecture

Modern CMS based on Wagtail, optimized for AWS architecture with multi-service container approach.

## 🏗️ Architecture

### Macro Architecture

```
🌍 Global Users → 📡 CloudFront CDN → 📦 S3 Static Landing
                                    ↓
                            🖥️ All-in-One Wagtail Container
                                    ↓
                    🗄️ Aurora Serverless v2 + S3 Media Storage
```

### Micro Architecture (Multi-Service Container)

```
🐳 All-in-One Smart Container
├─ 🖥️ Wagtail CMS (Port 8000)
├─ 🔌 FastAPI Service (Port 8001)
├─ ⚙️ Celery Background Worker
└─ 🌐 Nginx Reverse Proxy (Port 80)
```

## 💰 Cost: $15.50/month

- **S3 Static + Media**: $1.00/month
- **CloudFront CDN**: $1.00/month
- **Wagtail Container (Fargate)**: $7.00/month
- **Aurora Serverless v2**: $7.00/month
- **GitHub Actions**: $0.00/month (free tier)

## 🚀 Quick Start

### 1. Local Development

```bash
# Clone repository
git clone <your-repo>
cd Blog_landing_p

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run with Docker Compose
docker-compose up --build
```

### 2. Quick Setup (Recommended)

```bash
# After cloning, run the setup script
python setup.py

# This will automatically:
# - Install dependencies
# - Apply migrations
# - Create admin user
# - Set up HomePage
```

### 3. Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### 4. Access to Applications

- **Website**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **API**: http://localhost:8000/api/
- **MinIO (S3)**: http://localhost:9001/
- **PostgreSQL**: localhost:5432

## 🐳 Multi-Service Container

### Supervisord manages 4 processes:

1. **Nginx** (Port 80) - Reverse proxy + static files
2. **Wagtail** (Port 8000) - Django CMS
3. **FastAPI** (Port 8001) - High-performance API
4. **Celery** - Background tasks + content export

### Benefits:

- ✅ One container = easier deployment
- ✅ Automatic process restart
- ✅ Unified logging
- ✅ Efficient resource usage

## ☁️ AWS Production Deployment

### 1. Infrastructure

```bash
# Create ECR repository
aws ecr create-repository --repository-name landing-page-cms

# Create ECS cluster
aws ecs create-cluster --cluster-name landing-page-cms-cluster

# Create Aurora Serverless v2
aws rds create-db-cluster \
  --db-cluster-identifier landing-page-cms \
  --engine aurora-postgresql \
  --serverless-v2-scaling-configuration MinCapacity=0.5,MaxCapacity=2
```

### 2. S3 Buckets

- `wagtail-static-site` - static site
- `wagtail-media` - media files
- Intelligent Tiering for automatic optimization

### 3. CloudFront Distribution

- HTTP/3 + Brotli compression
- Global edge locations
- DDoS protection enabled

## 🔄 CI/CD Pipeline

### GitHub Actions automatically:

1. 🧪 Runs tests
2. 🐳 Builds Docker image
3. 📤 Pushes to Amazon ECR
4. 🚀 Deploys to ECS
5. 📦 Exports content to S3
6. 🗑️ Invalidates CloudFront cache

## 📊 Monitoring and Health Checks

### Endpoints:

- `/health/` - general health check
- `/admin/login/` - Wagtail health
- `/api/health/` - FastAPI health
- Queue depth monitoring for Celery

## 🔧 Configuration

### Environment Variables:

```bash
# Database
DB_NAME=landing_page_cms
DB_USER=postgres
DB_PASSWORD=<password>
DB_HOST=<aurora-endpoint>

# AWS
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>
AWS_STORAGE_BUCKET_NAME=wagtail-media
AWS_S3_REGION_NAME=us-east-1

# Celery
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

## 📈 Performance Features

- **In-memory caching** for API responses
- **Connection pooling** for Aurora
- **Gzip + Brotli compression** in Nginx
- **Rate limiting** for API endpoints
- **Background image optimization**
- **Smart content export** only for changed files

## 🛡️ Security

- **Content Security Policy (CSP)**
- **Rate limiting** on API endpoints
- **HTTPS only** in production
- **VPC isolation** for Aurora
- **IAM roles** for ECS tasks

## 🔍 Troubleshooting

### Logs:

```bash
# Supervisord
docker exec <container> tail -f /var/log/supervisor/supervisord.log

# Wagtail
docker exec <container> tail -f /var/log/supervisor/wagtail.err.log

# FastAPI
docker exec <container> tail -f /var/log/supervisor/fastapi.err.log

# Nginx
docker exec <container> tail -f /var/log/nginx/error.log
```

### Health Checks:

```bash
# Check all services
curl http://localhost:8000/health/
curl http://localhost:8000/admin/login/
curl http://localhost:8000/api/health/
```

## 📚 Documentation

- [Wagtail Documentation](https://docs.wagtail.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [AWS ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [Frontend Setup Guide](FRONTEND_SETUP.md) - For frontend developers

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.
