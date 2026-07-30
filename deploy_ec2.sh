#!/bin/bash
# ==============================================================================
# StudyVerse — AWS EC2 One-Command Automated Deployment Script (Ubuntu 22.04/24.04)
# ==============================================================================

set -e

echo "🚀 Starting StudyVerse AWS EC2 Deployment..."

# 1. Update System & Install Dependencies
echo "📦 Installing system packages (Python, MySQL, Nginx, Git)..."
sudo apt update -y
sudo apt install -y python3-pip python3-venv python3-dev default-libmysqlclient-dev build-essential pkg-config mysql-server nginx git curl

# 2. Start & Configure MySQL
echo "🗄️ Setting up MySQL database 'notehub_db'..."
sudo systemctl enable --now mysql
sudo mysql -e "CREATE DATABASE IF NOT EXISTS notehub_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
sudo mysql -e "CREATE USER IF NOT EXISTS 'notehub_user'@'localhost' IDENTIFIED BY 'StudyVerse2026!';"
sudo mysql -e "GRANT ALL PRIVILEGES ON notehub_db.* TO 'notehub_user'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"

# 3. Setup Project Directory & Virtual Environment
PROJECT_DIR="/var/www/StudyVerse"
echo "📂 Setting up project directory at $PROJECT_DIR..."
sudo mkdir -p $PROJECT_DIR
sudo chown -R $USER:$USER $PROJECT_DIR

if [ ! -d "$PROJECT_DIR/.git" ]; then
    echo "📥 Cloning StudyVerse repository from GitHub..."
    git clone https://github.com/Ayush12708/e-notes-sharing-application.git $PROJECT_DIR
else
    echo "🔄 Pulling latest code from GitHub..."
    cd $PROJECT_DIR
    git pull origin main
fi

cd $PROJECT_DIR

# 4. Virtual Environment & Dependencies
echo "🐍 Creating Python virtual environment and installing dependencies..."
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt
./venv/bin/pip install gunicorn pymysql

# 5. Database Migrations & Static Files
echo "⚡ Running Django migrations and collecting static files..."
export DB_HOST="localhost"
export DB_NAME="notehub_db"
export DB_USER="notehub_user"
export DB_PASSWORD="StudyVerse2026!"
export DB_PORT="3306"

./venv/bin/python manage.py migrate
./venv/bin/python manage.py collectstatic --noinput

# 6. Configure Systemd Gunicorn Service
echo "⚙️ Creating Gunicorn systemd service..."
sudo bash -c "cat <<EOF > /etc/systemd/system/studyverse.service
[Unit]
Description=StudyVerse Gunicorn Daemon
After=network.target mysql.service

[Service]
User=$USER
Group=www-data
WorkingDirectory=$PROJECT_DIR
Environment=\"PATH=$PROJECT_DIR/venv/bin\"
Environment=\"DB_HOST=localhost\"
Environment=\"DB_NAME=notehub_db\"
Environment=\"DB_USER=notehub_user\"
Environment=\"DB_PASSWORD=StudyVerse2026!\"
Environment=\"DB_PORT=3306\"
ExecStart=$PROJECT_DIR/venv/bin/gunicorn --workers 3 --bind unix:$PROJECT_DIR/studyverse.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
EOF"

sudo systemctl daemon-reload
sudo systemctl enable --now studyverse.service
sudo systemctl restart studyverse.service

# 7. Configure Nginx Web Server
echo "🌐 Configuring Nginx reverse proxy..."
sudo bash -c "cat <<EOF > /etc/nginx/sites-available/studyverse
server {
    listen 80;
    server_name _;

    client_max_body_size 50M;

    location /static/ {
        alias $PROJECT_DIR/staticfiles/;
    }

    location /media/ {
        alias $PROJECT_DIR/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:$PROJECT_DIR/studyverse.sock;
    }
}
EOF"

sudo ln -sf /etc/nginx/sites-available/studyverse /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

echo "
==============================================================================
🎉 StudyVerse AWS EC2 Deployment Complete!
==============================================================================
🌐 Public URL: http://$(curl -s ifconfig.me)
🗄️ MySQL DB: notehub_db (User: notehub_user)
⚙️ Service: studyverse.service
==============================================================================
"
