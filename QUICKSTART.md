# 🚀 Quick Start Guide

## Локальная разработка

### 1. Активация окружения

```bash
.\venv\Scripts\Activate.ps1
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка базы данных

```bash
# Создать .env файл из примера
copy env.example .env

# Выполнить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
```

### 4. Запуск Django сервера

```bash
python manage.py runserver
```

## Docker Compose (рекомендуется)

### 1. Запуск всех сервисов

```bash
docker-compose up --build
```

### 2. Доступ к сервисам

- **Сайт**: http://localhost:8000/
- **Админ-панель**: http://localhost:8000/admin/
- **API**: http://localhost:8000/api/
- **MinIO (S3)**: http://localhost:9001/
- **PostgreSQL**: localhost:5432

## Тестирование

### Проверка FastAPI

```bash
python -c "from landing_page_cms.api import app; print('FastAPI OK')"
```

### Проверка Celery

```bash
python -c "from landing_page_cms.celery import app; print('Celery OK')"
```

### Health Checks

```bash
curl http://localhost:8000/health/
curl http://localhost:8000/admin/login/
curl http://localhost:8000/api/health/
```

## Структура проекта

```
landing_page_cms/
├── 🐳 Dockerfile (multi-service container)
├── 🐙 docker-compose.yml (локальная разработка)
├── ⚙️ docker/ (конфигурации)
│   ├── supervisord.conf (управление процессами)
│   ├── nginx.conf (reverse proxy)
│   └── celery.conf (background tasks)
├── 🚀 .github/workflows/ (CI/CD)
├── 🔌 landing_page_cms/api.py (FastAPI)
├── ⚙️ landing_page_cms/celery.py (Celery)
└── ⚙️ landing_page_cms/settings/ (Django настройки)
    ├── base.py
    ├── development.py
    └── production.py (AWS оптимизированные)
```

## Следующие шаги

1. **Настройка AWS**: Создать S3 buckets и Aurora database
2. **Деплой**: Настроить GitHub Actions secrets
3. **Мониторинг**: Добавить CloudWatch метрики
4. **Масштабирование**: Настроить auto-scaling в ECS
