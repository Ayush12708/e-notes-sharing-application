# 📚 NoteHub – Simple E-Notes Sharing Platform

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Vanilla-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> **NoteHub** is a full-fledged, modern web application designed for university and college students to seamlessly share, discover, type, draw, and download academic study notes, lecture guides, and exam preparation materials.

---

## 🌟 Key Features & Highlights

### 🎨 1. Modern Glassmorphic UI & Responsive Design
- Clean, state-of-the-art UI featuring CSS custom properties, glassmorphism, responsive data tables, status badges, and smooth micro-animations.
- Interactive user nameplate header dropdown popup menu with instant profile editing and one-click logout.

### ✍️ 2. Unified Note Creation & Drawing Studio
- **All-in-One Creation Form**: Combines text notes, whiteboard drawings, and file attachments in a single workspace.
- **🎨 Interactive Digital Whiteboard**:
  - HTML5 Canvas supporting Paint Brush drawing, custom color swatches, adjustable stroke sizes (Thin, Medium, Thick), and Eraser tool.
  - Supports mouse drawing and touchscreens (tablets & smartphones).
- **📤 Multi-Format Document Uploads**: Supports PDFs, Images (`.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`), Word (`.docx`), PowerPoint (`.pptx`), Text (`.txt`), and ZIP archives.

### 🛡️ 3. Unsaved Changes Guard & Save as Draft
- **Quit Protection Guard**: Displays a modal alert (`⚠️ Unsaved Changes`) if a user attempts to leave the page with uncommitted edits.
- **Tab Close Warning**: Protects against accidental tab closing or reloading (`beforeunload`).
- **💾 Save as Draft**: Allows students to save progress as drafts (`📝 Draft`) and resume editing later.

### 📊 4. Academic Discovery Dashboard & Metrics
- **6 Real-time Analytics Cards**: Total Uploads, Approved Notes, Pending Reviews, Rejected Submissions, Total Downloads Received, and Saved Bookmarks Count.
- **🏷️ Subject Category Explorer**: 1-click exploration for core engineering and academic subjects (DSA, DBMS, OS, Computer Networks, Python, Java).
- **💖 Bookmarks & Upvotes**: Bookmark essential materials for revision and upvote high-quality notes.
- **💬 Student Comment Discussions**: Public discussion thread under each study note.

### 🔒 5. Landing Page Preview & Account Protection
- **🔥 Trending Courses Preview**: Showcases trending course notes on the public home page.
- **🔒 Protected Access Guard**: Guests can preview titles and metadata, but attempting to view or download full documents requires logging in or creating a free account.

### 🛡️ 6. Admin Verification Workflow
- Admin Dashboard for reviewing, approving, or rejecting submitted study materials before publication.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.13, Django 6.0
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), JavaScript (ES6+ HTML5 Canvas API)
- **Database**: SQLite / MySQL fallback
- **Authentication**: Django Auth & Database-backed Session Engine (Supports concurrent logins)

---

## 📁 Repository Directory Structure

```
NoteHub/
├── accounts/               # User authentication, profile management, and forms
├── config/                 # Project configuration & settings (settings.py, urls.py)
├── dashboard/              # User dashboard, statistics calculations, & analytics
├── home/                   # Landing page, public previews, & about section
├── notes/                  # Core notes model, views, forms, whiteboard canvas & comment views
│   ├── migrations/         # Database migration scripts
│   ├── models.py           # Note, Bookmark, and Comment models
│   ├── views.py            # Notes browsing, detail, creation, & download logic
│   └── forms.py            # Unified NoteForm & validation
├── static/                 # Stylesheets (style.css) and client-side JavaScript
├── templates/              # HTML templates (base, home, dashboard, notes, accounts)
├── manage.py               # Django CLI utility script
└── README.md               # Project documentation
```

---

## 🚀 Getting Started & Local Installation

Follow these steps to run NoteHub locally on your machine:

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
pip install django
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Local Development Server
```bash
python manage.py runserver 8000
```
Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📝 License

This project is licensed under the MIT License. Feel free to use and contribute!
