# 🎨 Frontend Developer Setup Guide

This guide will help frontend developers get started with the Landing Page CMS project.

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <your-repository>
cd Blog_landing_p

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup (IMPORTANT!)
```bash
# Apply database migrations
python manage.py migrate

# Create your own admin user (REQUIRED!)
python manage.py createsuperuser
# Enter username, email, and password when prompted
```

### 3. Run the Project
```bash
# Start Django server
python manage.py runserver

# Open in browser
http://127.0.0.1:8000/
```

## ⚠️ Important Notes

### 🔑 Admin Access:
- **Each developer must create their own admin user**
- **Your admin credentials won't work for others**
- **Run `python manage.py createsuperuser` after setup**

### 🗄️ Database:
- **Always run `python manage.py migrate` after pulling changes**
- **Each developer has their own local database**
- **No shared data between developers**

## 🎯 What's Ready for Frontend

### ✅ Backend is Complete:
- **Django + Wagtail CMS** - Full backend API
- **StreamField Models** - Flexible content blocks
- **Admin Panel** - Content management interface
- **Database Models** - All data structures ready
- **URL Routing** - All endpoints configured

### 🎨 Frontend Components Ready:
- **CSS Framework** - `static/css/home_page.css`
- **HTML Templates** - `home/templates/home/home_page.html`
- **Responsive Design** - Mobile-first approach
- **Modern UI** - Clean, professional design

## 📱 Content Blocks Available

### 1. **Hero Section**
- Title, subtitle, button
- Background image support
- CTA button with custom URL

### 2. **Rich Text**
- Full text editor
- HTML formatting
- Responsive typography

### 3. **Image Gallery**
- Image uploads
- Caption support
- Responsive sizing

### 4. **Features List**
- Title and description
- Icon support
- Grid layout

### 5. **Testimonials**
- Customer reviews
- Author name and position
- Quote styling

### 6. **Contact Form**
- Name, email, message fields
- Form validation
- Submit functionality

## 🔧 How to Add Content

### Via Admin Panel:
1. Go to http://127.0.0.1:8000/admin/
2. Login with **YOUR** superuser account
3. Find "Home" page
4. Edit content in StreamField
5. Save and preview

### Via Code:
- Edit `home/templates/home/home_page.html`
- Modify `static/css/home_page.css`
- Add new content blocks in `home/models.py`

## 🎨 Customization

### CSS Variables:
```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  --accent-color: #e74c3c;
  --text-color: #333;
  --light-bg: #f8f9fa;
}
```

### Adding New Blocks:
1. Create new model in `home/models.py`
2. Add to StreamField configuration
3. Create template for the block
4. Add CSS styling

## 📱 Responsive Breakpoints

- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🚀 Deployment Ready

- **Docker support** - `docker-compose.yml`
- **AWS ready** - CloudFormation templates
- **CI/CD** - GitHub Actions configured
- **Production settings** - Separate config files

## ❓ Need Help?

- Check Django logs in terminal
- Review Wagtail documentation
- Check browser console for errors
- Verify database migrations

## 🔗 Useful Links

- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Wagtail Docs**: https://docs.wagtail.org/
- **Django Docs**: https://docs.djangoproject.com/
- **Project README**: README.md
