#!/usr/bin/env python
"""
Quick Setup Script for Landing Page CMS
Run this script after cloning the repository to set up your development environment.
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and show progress"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🚀 Landing Page CMS - Quick Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("manage.py"):
        print("❌ Error: manage.py not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Step 1: Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("❌ Failed to install dependencies. Please check your Python environment.")
        sys.exit(1)
    
    # Step 2: Apply migrations
    if not run_command("python manage.py migrate", "Applying database migrations"):
        print("❌ Failed to apply migrations. Please check your database configuration.")
        sys.exit(1)
    
    # Step 3: Create superuser
    print("\n🔑 Creating admin user...")
    print("Please enter the following information:")
    
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    
    if not username or not email:
        print("❌ Username and email are required!")
        sys.exit(1)
    
    # Create superuser non-interactively
    create_user_cmd = f'python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(\'{username}\', \'{email}\', \'admin123\') if not User.objects.filter(username=\'{username}\').exists() else None; print(\'User created successfully!\' if not User.objects.filter(username=\'{username}\').exists() else \'User already exists!\')"'
    
    if not run_command(create_user_cmd, "Creating admin user"):
        print("❌ Failed to create admin user. You can create it manually with:")
        print("   python manage.py createsuperuser")
    
    # Step 4: Create HomePage if it doesn't exist
    print("\n🏠 Checking HomePage...")
    check_homepage_cmd = 'python manage.py shell -c "from home.models import HomePage; print(\'HomePage exists!\' if HomePage.objects.exists() else \'No HomePage found. Creating one...\'); HomePage.objects.get_or_create(title=\'Home\', slug=\'home\', defaults={\'title\': \'Home\', \'slug\': \'home\'})"'
    
    if not run_command(check_homepage_cmd, "Checking HomePage"):
        print("⚠️  Warning: Could not check HomePage. You may need to create it manually.")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Start the server: python manage.py runserver")
    print("2. Open http://127.0.0.1:8000/ in your browser")
    print("3. Login to admin panel: http://127.0.0.1:8000/admin/")
    print("   Username: " + username)
    print("   Password: admin123")
    print("\n⚠️  Important: Change the default password after first login!")
    print("\n🔗 Useful links:")
    print("- Frontend Setup Guide: FRONTEND_SETUP.md")
    print("- Project README: README.md")

if __name__ == "__main__":
    main()
