# 🚀 StudyVerse – Empowering Minds, Sharing Knowledge

[![AWS EC2 Live](https://img.shields.io/badge/AWS-EC2%20Live%20Demo-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](http://23.20.190.164)
[![AWS RDS MySQL](https://img.shields.io/badge/AWS-RDS%20MySQL%208.0-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white)](http://23.20.190.164)
[![AWS S3 Storage](https://img.shields.io/badge/AWS-S3%20Bucket%20Uploads-569A31?style=for-the-badge&logo=amazons3&logoColor=white)](http://23.20.190.164)
[![Vercel Deployment](https://img.shields.io/badge/Vercel-Live%20Demo-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://e-notes-sharing-application.vercel.app)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayush12708/e-notes-sharing-application)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

> 🌐 **AWS EC2 Production Live App**: [http://23.20.190.164](http://23.20.190.164)  
> 🗄️ **AWS RDS Production Database**: `dbstudyverse.c6nwkq8cuodu.us-east-1.rds.amazonaws.com`  
> 🪣 **AWS S3 File Storage Bucket**: `studyverse-uploads` (`us-east-1`)  
> ⚡ **Vercel Live App**: [https://e-notes-sharing-application.vercel.app](https://e-notes-sharing-application.vercel.app)  
> 📄 **Project PDF Report**: [StudyVerse_Project_Report.pdf](./StudyVerse_Project_Report.pdf)  
>
> **StudyVerse** (*"Empowering Minds, Sharing Knowledge"*) is a full-stack, enterprise-grade web application designed for university students to upload, create, search, bookmark, and discuss academic study notes, lecture guides, and exam preparation materials in real-time.

---

## 🔑 Demo Account Credentials

You can log into the live AWS application instantly using any of the following accounts:

| Username | Password | Account Role | Access Rights |
| :--- | :--- | :--- | :--- |
| **`admin`** | **`admin123`** | **Admin / Superuser** | Access to [🛠 Admin Moderation Panel](http://23.20.190.164/notes/admin-dashboard/) |
| **`ayush`** | **`ayush123`** | Student User | Upload notes, e-note whiteboard, bookmarks, comments |
| **`bala`** | **`bala123`** | Student User | Upload notes, e-note whiteboard, bookmarks, comments |

*Or register a new account on [http://23.20.190.164/accounts/register/](http://23.20.190.164/accounts/register/)!*

---

## 🌟 Key Features & Architectural Highlights

### 🛠️ 1. Complete Cloud Infrastructure (AWS EC2 + AWS RDS MySQL)
- **AWS EC2 Virtual Server (`23.20.190.164`)**: Runs Ubuntu 24.04, Nginx 1.24 reverse proxy, Gunicorn WSGI daemon (`studyverse.service`), and WhiteNoise static asset pipeline.
- **AWS RDS MySQL 8.0 (`dbstudyverse...`)**: Production relational database instance storing all users, profile metadata, notes, bookmarks, comments, and sessions.
- **1-Command Deployment Script ([`deploy_ec2.sh`](./deploy_ec2.sh))**: Automated shell script to provision system packages, MySQL schema, Gunicorn systemd service, and Nginx configuration.

### 🎨 2. Seamless Single-Card UI & Sober Academic Aesthetics
- **Sober Academic Theme**: Professional slate and royal blue palette (`#1e293b` & `#2563eb`) tailored for academic focus.
- **Unified Single-Card Auth Pages**: Centered, partition-free login and registration cards with brand badges and high-contrast typography.

### 🛡️ 3. Admin Content Moderation & Verification Workflow
- **Interactive Status Filters**: Filter submissions by **All**, **⏳ Pending**, **✔ Approved**, **✖ Rejected**, and **📝 Drafts**.
- **Document Preview Button (`👁 View Note`)**: Allows admins to inspect uploaded files or digital e-notes before approving or rejecting.
- **4-State Moderation Lifecycle**: `Draft` → `Pending` → `Approved` / `Rejected`.

### ✍️ 4. Digital E-Notes Studio & Interactive Whiteboard Canvas
- **E-Notes Studio (`/notes/create-online/`)**: Type, format, and publish digital code cheatsheets and lecture notes.
- **🎨 Interactive Whiteboard Canvas**: Draw diagrams using Paint Brush, color swatches, adjustable stroke widths, and Eraser tool.
- **📤 Document Upload (`/notes/upload/`)**: Upload PDF, Word (`.docx`), PowerPoint (`.pptx`), Images (`.png`), Text (`.txt`), and ZIP files.

### ⚡ 5. Real-Time View Counter & Social Features
- **Atomic Real-Time View Counter**: Uses Django `F()` expressions (`UPDATE notes_note SET views = views + 1`) to eliminate race conditions on high concurrency.
- **❤️ Bookmarks & Likes**: Save favorite notes with instant AJAX updates and dedicated Bookmarks page.
- **💬 Student Discussion Threads**: Interactive comment section on note detail pages.
- **🔄 Django Signals (`accounts/signals.py`)**: `post_save` signal on `User` model automatically creates profile records regardless of creation origin (web, admin, shell, workbench).

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.12, Django 6.0 | Server-side logic, ORM, authentication |
| **Database** | AWS RDS MySQL 8.0, PyMySQL | Production database instance |
| **Web Server** | Nginx 1.24, Gunicorn WSGI | Reverse proxy & application server |
| **Cloud Hosting** | AWS EC2 (Ubuntu 24.04), Vercel | Infrastructure & serverless hosting |
| **Frontend** | HTML5, Vanilla CSS3, JavaScript | Modern responsive design system |
| **Tooling** | MySQL Workbench, Git, PDFKit/FPDF2 | Database management & project report generation |

---

## 📁 Repository Directory Structure

```
NoteHub/
├── accounts/               # User authentication, profiles, signals, & forms
├── config/                 # Project configuration (settings.py, urls.py, wsgi.py)
├── dashboard/              # Student dashboard & real-time analytics aggregation
├── home/                   # Landing page, public previews, & department grid
├── notes/                  # Core note models, whiteboard canvas, views, & moderation
├── static/                 # Custom CSS design system (1300+ lines) & JavaScript
├── templates/              # HTML templates (base, home, dashboard, notes, accounts)
├── deploy_ec2.sh           # Automated 1-command AWS EC2 deployment script
├── generate_report_pdf.py  # Standalone FPDF2 PDF project report generator
├── vercel.json             # Vercel serverless deployment routing config
├── StudyVerse_Project_Report.md  # Detailed markdown project report
├── StudyVerse_Project_Report.pdf # Formatted PDF project report
├── manage.py               # Django CLI management tool
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ayush12708/e-notes-sharing-application.git
cd e-notes-sharing-application
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver 8000
```
Navigate to `http://127.0.0.1:8000/`.

---

## 🌐 Live Production Links

- 🚀 **AWS EC2 Web App**: [http://23.20.190.164](http://23.20.190.164)
- 🗄️ **AWS RDS MySQL Host**: `dbstudyverse.c6nwkq8cuodu.us-east-1.rds.amazonaws.com`
- ⚡ **Vercel Web App**: [https://e-notes-sharing-application.vercel.app](https://e-notes-sharing-application.vercel.app)
- 📄 **PDF Project Report**: [StudyVerse_Project_Report.pdf](./StudyVerse_Project_Report.pdf)

---

## 📝 License

This project is licensed under the MIT License. Developed by **Ayush Kumar** (Lovely Professional University).
