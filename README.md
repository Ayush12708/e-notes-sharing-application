# 📚 NoteHub – E-Notes Sharing & Digital Study Platform

[![Live Website](https://img.shields.io/badge/Render-Live%20Demo-brightgreen?style=for-the-badge&logo=render&logoColor=white)](https://notehub-vthi.onrender.com/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayush12708/e-notes-sharing-application)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Vanilla-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> 🚀 **Live Production Deployment**: [https://notehub-vthi.onrender.com/](https://notehub-vthi.onrender.com/)
> 
> **NoteHub** is a modern, full-featured web application designed for university students to share, discover, type, draw, and download academic study notes, lecture guides, and exam preparation materials in real-time.

---

## 🔑 Demo Account Credentials

You can test the live application instantly on Render using any of the following accounts:

| Username | Password | Account Role |
| :--- | :--- | :--- |
| **`ayush`** | **`ayush123`** | Student User |
| **`admin`** | **`admin123`** | Admin / Superuser |
| **`bala`** | **`bala123`** | Student User |

*Or register a new account on [https://notehub-vthi.onrender.com/accounts/register/](https://notehub-vthi.onrender.com/accounts/register/) (auto-logs in immediately upon registration)!*

---

## 🌟 Key Features & Highlights

### 🎨 1. Modern Glassmorphic UI & Responsive Design
- Clean, state-of-the-art UI featuring CSS custom properties, glassmorphism, responsive data tables, status badges, and micro-animations.
- User dropdown header menu with profile editing and single-click logout.

### ✍️ 2. Dedicated E-Notes Studio & Interactive Whiteboard Canvas
- **Digital E-Notes Creation Studio (`/notes/create-online/`)**: Type, format, and publish digital notes, definitions, and code cheatsheets.
- **🎨 Interactive Whiteboard Canvas**: Sketch handwritten diagrams with Paint Brush, custom color swatches, adjustable stroke sizes (Thin, Medium, Thick), and Eraser tool.
- **📤 Document File Upload (`/notes/upload/`)**: Dedicated basic upload page supporting PDFs, Word (`.docx`), PowerPoint (`.pptx`), Images (`.png`, `.jpg`), Text (`.txt`), and ZIP archives.

### 🛡️ 3. Unsaved Changes Guard & Save as Draft
- **Quit Protection Guard**: Custom modal alert (`⚠️ Unsaved Changes`) prevents accidental navigation or tab closing when editing notes without saving.
- **💾 Save as Draft**: Students can save progress as drafts (`📝 Draft`) and resume editing at any time.

### ⚡ 4. 100% Real-Time Likes & Downloads Analytics
- **Live Downloads Counter**: Real-time counter increments whenever a document is viewed or downloaded.
- **❤️ Dynamic Likes & Bookmarks**: Track genuine upvotes and saved bookmarks with live updates.
- **💬 Student Comment Discussions**: Interactive comment threads on each study note.

### 🛡️ 5. Admin Approval & Verification Workflow
- All new user submissions undergo Admin review (`Pending` status) before being publicly visible in `Browse Notes`.
- Staff members can approve or reject submissions from the **[🛠 Admin Panel](https://notehub-vthi.onrender.com/notes/admin-dashboard/)**.

### 🔒 6. Landing Page & Course Previews
- Guests can preview course note titles and subject categories on the home page.
- Opening full materials requires logging in or creating a free account.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.13, Django 6.0
- **Production Server**: Gunicorn, Whitenoise (Static Asset Serving)
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), JavaScript (ES6+ HTML5 Canvas API)
- **Database**: SQLite / PostgreSQL compatible
- **Deployment Platform**: Render (`https://notehub-vthi.onrender.com/`)

---

## 📁 Repository Directory Structure

```
NoteHub/
├── accounts/               # User authentication, profiles, & forms
├── config/                 # Project configuration (settings.py, urls.py, wsgi.py)
├── dashboard/              # User dashboard & real-time analytics calculations
├── home/                   # Landing page, public previews, & about section
├── notes/                  # Core note models, views, whiteboard canvas, & comment logic
│   ├── migrations/         # Database migrations
│   ├── models.py           # Note, Bookmark, & Comment models
│   ├── views.py            # Notes views & approval handlers
│   └── forms.py            # NoteForm & OnlineNoteForm
├── static/                 # CSS stylesheets & JS scripts
├── templates/              # HTML templates (base, home, dashboard, notes, accounts)
├── manage.py               # Django CLI utility script
├── render.yaml             # Render deployment configuration
├── build.sh                # Render build script
└── README.md               # Project documentation
```

---

## 🚀 Getting Started & Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Ayush12708/e-notes-sharing-application.git
cd e-notes-sharing-application
```

### 2. Create and Activate Virtual Environment
```bash
# On macOS / Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django whitenoise gunicorn
```

### 4. Run Database Migrations & Seed Data
```bash
python manage.py migrate
```

### 5. Run the Local Server
```bash
python manage.py runserver 8000
```
Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🌐 Live Application URL

- **Live Website**: [https://notehub-vthi.onrender.com/](https://notehub-vthi.onrender.com/)
- **GitHub Repository**: [https://github.com/Ayush12708/e-notes-sharing-application](https://github.com/Ayush12708/e-notes-sharing-application)

---

## 📝 License

This project is licensed under the MIT License. Feel free to use, modify, and contribute!
