# StudyVerse — E-Notes Sharing Application
## Detailed Project Report

---

**Project Title:** StudyVerse — E-Notes Sharing Application  
**Developed By:** Ayush Kumar  
**University:** Lovely Professional University (LPU)  
**Course:** B.Tech Computer Science Engineering  
**Semester:** 7th Semester  
**GitHub:** https://github.com/Ayush12708/e-notes-sharing-application  
**Date:** July 2026  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Problem Statement](#2-problem-statement)
3. [Objectives](#3-objectives)
4. [Technology Stack](#4-technology-stack)
5. [System Architecture](#5-system-architecture)
6. [Database Design (ER Diagram & Schema)](#6-database-design)
7. [Module Description](#7-module-description)
8. [Functional Requirements](#8-functional-requirements)
9. [Non-Functional Requirements](#9-non-functional-requirements)
10. [Implementation Details](#10-implementation-details)
11. [URL Routing Structure](#11-url-routing-structure)
12. [Screenshots & User Interface](#12-screenshots--user-interface)
13. [Testing & Validation](#13-testing--validation)
14. [Future Scope](#14-future-scope)
15. [Conclusion](#15-conclusion)

---

## 1. Introduction

**StudyVerse** is a full-stack web-based E-Notes Sharing Application designed to allow college and university students to upload, share, browse, and manage academic study materials such as lecture notes, PDF documents, and digitally-created e-notes. The platform enables peer-to-peer knowledge exchange across multiple engineering branches and semesters with features like bookmarking, commenting, likes, admin content moderation, and real-time view tracking.

The application follows the **Django MVT (Model-View-Template)** architectural pattern and uses **MySQL** as its production database managed via MySQL Workbench, making it a robust, scalable, and secure platform for academic collaboration.

**Tagline:** *"Empowering Minds, Sharing Knowledge"*

---

## 2. Problem Statement

College students often face significant challenges in accessing quality study materials:

- **Fragmented Resources:** Notes are scattered across WhatsApp groups, Google Drive links, and personal devices with no centralized access point.
- **No Quality Control:** Shared materials often lack verification, leading to incorrect or incomplete content being circulated before exams.
- **Limited Discovery:** Students struggle to find notes for specific subjects, semesters, or branches — especially across different colleges.
- **No Collaboration:** Traditional file sharing provides no mechanism for discussions, feedback, or community-driven quality improvement.
- **Loss of Materials:** Students frequently lose access to important notes when WhatsApp groups are deleted or Drive links expire.

**StudyVerse solves these problems** by providing a permanent, centralized, admin-verified platform where students can upload, discover, bookmark, and discuss study materials with real-time analytics.

---

## 3. Objectives

1. **Centralized Note Repository** — Build a single platform where students from any branch can upload and access notes.
2. **Multi-Format Support** — Support file uploads (PDF, DOCX, PPTX, images) and online rich-text e-note creation with a whiteboard drawing canvas.
3. **Admin Content Moderation** — Implement a verification workflow (Pending → Approved / Rejected) ensuring content quality.
4. **Smart Search & Filtering** — Enable students to find notes by subject, branch, semester, keyword search, and sorting options.
5. **Social Engagement Features** — Allow users to like, bookmark, and comment on notes to foster academic discussion.
6. **Real-Time Analytics** — Track note view counts and display live statistics on the platform.
7. **Multi-User Authentication** — Provide secure registration, login, profile management, and concurrent session handling.
8. **MySQL Integration** — Store all data in a production-grade MySQL database (managed via MySQL Workbench).

---

## 4. Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend Framework** | Django 5.x (Python) | Server-side logic, ORM, URL routing, authentication |
| **Frontend** | HTML5, CSS3, JavaScript | Templates, responsive UI, interactive components |
| **Database** | MySQL 8.0 (via MySQL Workbench) | Production data storage for users, notes, sessions |
| **MySQL Driver** | PyMySQL | Python interface to connect Django with MySQL |
| **CSS Framework** | Custom CSS Design System | 1300+ lines of hand-crafted responsive CSS |
| **Fonts** | Google Fonts (Poppins) | Modern typography across the platform |
| **Version Control** | Git + GitHub | Source code management and collaboration |
| **Deployment Config** | Gunicorn + WhiteNoise | Production WSGI server and static file serving |
| **IDE** | VS Code / Cursor IDE | Development environment |

### Python Dependencies (`requirements.txt`):
```
django
gunicorn
whitenoise
pymysql
```

---

## 5. System Architecture

### 5.1 Django MVT Architecture

```
┌──────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                   │
│         HTML/CSS/JS ← Django Templates               │
└──────────────────────┬───────────────────────────────┘
                       │ HTTP Request
                       ▼
┌──────────────────────────────────────────────────────┐
│                   URL DISPATCHER                      │
│              config/urls.py → App URLs                │
└──────────────────────┬───────────────────────────────┘
                       │ Route to View
                       ▼
┌──────────────────────────────────────────────────────┐
│                     VIEWS                             │
│    accounts/views.py | notes/views.py |               │
│    dashboard/views.py | home/views.py                 │
└──────────┬────────────────────────────┬──────────────┘
           │ Query Models               │ Render Template
           ▼                            ▼
┌─────────────────────┐    ┌──────────────────────────┐
│   MODELS (ORM)      │    │     TEMPLATES            │
│   User, Profile,    │    │   base.html, index.html  │
│   Note, Bookmark,   │    │   dashboard.html,        │
│   Comment           │    │   browse_notes.html, etc │
└─────────┬───────────┘    └──────────────────────────┘
          │ SQL Queries
          ▼
┌──────────────────────────────────────────────────────┐
│              MySQL DATABASE (notehub_db)              │
│     auth_user | accounts_profile | notes_note        │
│     notes_bookmark | notes_comment | django_session  │
└──────────────────────────────────────────────────────┘
```

### 5.2 Project Directory Structure

```
NoteHub/
├── config/                  # Project configuration
│   ├── settings.py          # Django settings (DB, apps, middleware)
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI entry point
│
├── accounts/                # User Authentication Module
│   ├── models.py            # Profile model (extends User)
│   ├── views.py             # Register, Login, Logout, Profile views
│   ├── forms.py             # RegisterForm, UserUpdateForm, ProfileUpdateForm
│   ├── signals.py           # Auto-create Profile on User creation
│   ├── admin.py             # Django admin with Profile inline
│   └── urls.py              # Auth URL routes
│
├── notes/                   # Core Notes Module
│   ├── models.py            # Note, Bookmark, Comment models
│   ├── views.py             # CRUD, Browse, Admin Dashboard, Like/Bookmark
│   ├── forms.py             # NoteForm, OnlineNoteForm
│   └── urls.py              # Notes URL routes
│
├── dashboard/               # Student Dashboard Module
│   ├── views.py             # Dashboard stats and data aggregation
│   └── urls.py              # Dashboard URL route
│
├── home/                    # Landing Page Module
│   ├── views.py             # Homepage with live stats
│   └── urls.py              # Home URL route
│
├── templates/               # HTML Templates
│   ├── base.html            # Master layout (navbar, footer)
│   ├── home/index.html      # Landing page
│   ├── accounts/            # login.html, register.html, profile.html
│   ├── dashboard/           # dashboard.html
│   └── notes/               # browse, detail, upload, edit, delete, etc.
│
├── static/
│   ├── css/style.css        # Complete design system (1300+ lines)
│   └── js/script.js         # Client-side interactivity
│
├── media/notes/             # Uploaded note files (PDF, DOCX, etc.)
├── manage.py                # Django management utility
└── requirements.txt         # Python dependencies
```

---

## 6. Database Design

### 6.1 Entity-Relationship (ER) Diagram

```
┌─────────────────┐       1:1        ┌──────────────────┐
│    auth_user     │─────────────────▶│ accounts_profile  │
│─────────────────│                   │──────────────────│
│ id (PK)         │                   │ id (PK)          │
│ username        │                   │ user_id (FK→User)│
│ password (hash) │                   │ phone            │
│ email           │                   │ college          │
│ first_name      │                   │ semester         │
│ last_name       │                   └──────────────────┘
│ is_staff        │
│ is_active       │
│ date_joined     │
└─────┬───────────┘
      │ 1:N
      ▼
┌─────────────────┐       N:M        ┌──────────────────┐
│   notes_note    │──────────────────▶│ notes_note_likes │
│─────────────────│                   │──────────────────│
│ id (PK)         │                   │ note_id (FK)     │
│ title           │                   │ user_id (FK)     │
│ subject         │                   └──────────────────┘
│ branch          │
│ semester        │       1:N        ┌──────────────────┐
│ description     │─────────────────▶│ notes_bookmark   │
│ content (text)  │                   │──────────────────│
│ drawing_data    │                   │ id (PK)          │
│ is_online_note  │                   │ user_id (FK)     │
│ file (upload)   │                   │ note_id (FK)     │
│ uploaded_by(FK) │                   │ created_at       │
│ uploaded_at     │                   └──────────────────┘
│ downloads       │
│ views           │       1:N        ┌──────────────────┐
│ status          │─────────────────▶│ notes_comment    │
└─────────────────┘                   │──────────────────│
                                      │ id (PK)          │
                                      │ note_id (FK)     │
                                      │ user_id (FK)     │
                                      │ text             │
                                      │ created_at       │
                                      └──────────────────┘
```

### 6.2 MySQL Table Schema

| Table Name | Fields | Description |
|-----------|--------|-------------|
| `auth_user` | id, username, password, email, first_name, last_name, is_staff, is_active, date_joined | Django's built-in user authentication table |
| `accounts_profile` | id, user_id (FK), phone, college, semester | Extended user profile (1:1 with auth_user) |
| `notes_note` | id, title, subject, branch, semester, description, content, drawing_data, is_online_note, file, uploaded_by_id (FK), uploaded_at, downloads, views, status | Core notes/study materials table |
| `notes_bookmark` | id, user_id (FK), note_id (FK), created_at | User's saved/bookmarked notes |
| `notes_comment` | id, note_id (FK), user_id (FK), text, created_at | Discussion comments on notes |
| `notes_note_likes` | id, note_id (FK), user_id (FK) | Many-to-many likes on notes |
| `django_session` | session_key, session_data, expire_date | Active user login sessions |

---

## 7. Module Description

### Module 1: Accounts (User Authentication & Profile Management)

| Feature | Description |
|---------|-------------|
| **Registration** | New users register with username, email, password, phone, college, and semester. Passwords are hashed using Django's PBKDF2 algorithm. |
| **Login** | Case-insensitive username matching with secure authentication. Supports redirect after login (`?next=` parameter). |
| **Logout** | Destroys session and redirects to home page. |
| **Profile Management** | Users can view and edit their personal details (name, email, phone, college, semester). |
| **Auto Profile Creation** | Django `post_save` signal automatically creates a Profile whenever a User is created — by any method (website, admin, MySQL Workbench, shell). |
| **Admin Integration** | Profile is displayed inline inside Django Admin's User edit page. |

### Module 2: Notes (Core CRUD & Content Management)

| Feature | Description |
|---------|-------------|
| **Upload File Note** | Upload PDF, DOCX, PPTX, image files with metadata (title, subject, branch, semester, description). |
| **Create Online E-Note** | Create rich-text notes directly in browser with a whiteboard drawing canvas for diagrams. |
| **Browse Notes** | Filter approved notes by subject, branch, semester, and keyword search. Sorting by newest, oldest, A-Z, popularity. |
| **Note Detail View** | Full note display with file preview (PDF inline, images), metadata, view count, likes, bookmarks, and comments section. |
| **Real-Time View Counter** | View count increments automatically using Django `F()` expression every time a note is opened. |
| **Edit Note** | Authors can edit their own notes (re-submits to admin for approval). |
| **Delete Note** | Authors can delete their own notes with confirmation page. |
| **Save Draft** | Users can save notes as "Draft" without submitting for review. |

### Module 3: Social Engagement

| Feature | Description |
|---------|-------------|
| **Bookmarks (Save/Unsave)** | Toggle bookmark on any note. AJAX-powered for seamless UX. Dedicated bookmarks page. |
| **Likes** | Toggle like/unlike on notes. AJAX response returns updated count. |
| **Comments** | Post discussion comments on note detail page. Ordered by newest first. |

### Module 4: Admin Content Moderation

| Feature | Description |
|---------|-------------|
| **Admin Dashboard** | Staff-only panel showing all notes with counts for Pending, Approved, and Rejected. |
| **Approve/Reject Workflow** | Admin can approve or reject any pending note. Only approved notes appear in Browse. |
| **Status Management** | 4-state workflow: Draft → Pending → Approved/Rejected. |

### Module 5: Dashboard (Student Analytics)

| Feature | Description |
|---------|-------------|
| **Personal Stats** | Total notes uploaded, approved count, pending count, total downloads, total likes received. |
| **Recent Notes** | Quick view of user's latest uploaded notes. |
| **Saved Bookmarks** | Recent bookmarked notes for quick access. |
| **Subject Exploration** | Browse by subject categories with live note counts. |
| **Community Feed** | Recently uploaded and popular notes from the community. |

### Module 6: Home (Landing Page)

| Feature | Description |
|---------|-------------|
| **Hero Section** | Brand showcase with tagline, live stats card showing total notes, views, subjects, and students. |
| **Departments Grid** | Quick navigation cards for Engineering branches (CSE, IT, ECE, ME, Civil, BCA/MCA). |
| **About Section** | Platform mission with 3-step workflow explanation. |
| **Trending Notes** | Preview of popular study materials (locked for non-authenticated users). |
| **Features Section** | Highlight of key platform capabilities. |
| **Stats Banner** | Full-width gradient banner with aggregate statistics. |
| **Multi-Column Footer** | Branch navigation, subject quick-jump dropdowns, and platform info. |

---

## 8. Functional Requirements

| ID | Requirement | Status |
|----|------------|--------|
| FR-01 | User can register with username, email, password, phone, college, and semester | ✅ Implemented |
| FR-02 | User can login with username and password (case-insensitive) | ✅ Implemented |
| FR-03 | User can view and update their profile information | ✅ Implemented |
| FR-04 | User can upload notes as PDF/DOCX/PPTX/Image files | ✅ Implemented |
| FR-05 | User can create online e-notes with rich text and whiteboard drawing | ✅ Implemented |
| FR-06 | User can browse approved notes with search, filter, and sort | ✅ Implemented |
| FR-07 | User can view full note details including inline file preview | ✅ Implemented |
| FR-08 | View counter increments in real-time when note is opened | ✅ Implemented |
| FR-09 | User can bookmark/unbookmark notes | ✅ Implemented |
| FR-10 | User can like/unlike notes | ✅ Implemented |
| FR-11 | User can post comments on notes | ✅ Implemented |
| FR-12 | User can edit/delete their own notes | ✅ Implemented |
| FR-13 | User can save notes as "Draft" without submitting | ✅ Implemented |
| FR-14 | Admin can view all notes in Admin Dashboard | ✅ Implemented |
| FR-15 | Admin can approve or reject pending notes | ✅ Implemented |
| FR-16 | All data stored in MySQL database (via MySQL Workbench) | ✅ Implemented |
| FR-17 | Auto-create Profile for users created by any method | ✅ Implemented |

---

## 9. Non-Functional Requirements

| Requirement | Implementation |
|------------|---------------|
| **Security** | Passwords hashed with PBKDF2_SHA256. CSRF protection on all POST forms. Login required decorators on sensitive views. Staff-only access for admin panel. |
| **Performance** | View counter uses Django `F()` expression for atomic DB updates (no race conditions). Lazy QuerySet evaluation. Select-related for optimized JOINs. |
| **Scalability** | MySQL production database. Concurrent session support with DB-backed sessions. Gunicorn multi-worker WSGI server. |
| **Responsiveness** | Fully responsive CSS with mobile breakpoints at 992px and 640px. Flexible grid layouts. |
| **Usability** | Clean academic blue color palette. Intuitive navigation. Flash messages for all user actions. |

---

## 10. Implementation Details

### 10.1 User Registration Flow

```python
# accounts/views.py — register()
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 1. Create User in auth_user table
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # 2. Create Profile in accounts_profile table
            Profile.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone', ''),
                college=form.cleaned_data.get('college', ''),
                semester=form.cleaned_data.get('semester', 1)
            )
            # 3. Auto-login the user
            login(request, user)
            return redirect('dashboard')
```

### 10.2 Django Signal for Auto-Profile Creation

```python
# accounts/signals.py
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(
            user=instance,
            defaults={'phone': '', 'college': 'Not specified', 'semester': 1}
        )
```

### 10.3 Real-Time View Counter (Atomic Update)

```python
# notes/views.py — note_detail()
if request.method == "GET":
    Note.objects.filter(pk=pk).update(views=F("views") + 1)
    note.refresh_from_db()
```
This uses Django's `F()` expression to perform an atomic SQL `UPDATE notes_note SET views = views + 1` — preventing race conditions when multiple users view the note simultaneously.

### 10.4 MySQL Database Connection

```python
# config/settings.py
import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notehub_db',
        'USER': 'root',
        'PASSWORD': '****',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 10.5 Content Moderation Workflow

```
  User uploads note
        │
        ▼
  Status = "Pending"
        │
        ▼
  Admin reviews in Admin Dashboard
        │
   ┌────┴────┐
   ▼         ▼
Approved   Rejected
   │
   ▼
Visible in Browse Notes
```

---

## 11. URL Routing Structure

| URL Pattern | View Function | Description |
|-------------|--------------|-------------|
| `/` | `home.views.home` | Landing page with hero, departments, stats |
| `/accounts/register/` | `accounts.views.register` | User registration |
| `/accounts/login/` | `accounts.views.login_view` | User login |
| `/accounts/logout/` | `accounts.views.logout_view` | User logout |
| `/accounts/profile/` | `accounts.views.profile_view` | View & edit profile |
| `/dashboard/` | `dashboard.views.dashboard` | Student dashboard |
| `/notes/upload/` | `notes.views.upload_note` | Upload file note |
| `/notes/create-online/` | `notes.views.create_online_note` | Create e-note |
| `/notes/browse/` | `notes.views.browse_notes` | Browse & search notes |
| `/notes/detail/<id>/` | `notes.views.note_detail` | View note details |
| `/notes/my-notes/` | `notes.views.my_notes` | User's uploaded notes |
| `/notes/edit/<id>/` | `notes.views.edit_note` | Edit own note |
| `/notes/delete/<id>/` | `notes.views.delete_note` | Delete own note |
| `/notes/bookmark/<id>/` | `notes.views.toggle_bookmark` | Save/unsave bookmark |
| `/notes/like/<id>/` | `notes.views.toggle_like` | Like/unlike note |
| `/notes/bookmarks/` | `notes.views.bookmarks_list` | View saved bookmarks |
| `/notes/admin-dashboard/` | `notes.views.admin_dashboard` | Admin moderation panel |
| `/notes/approve/<id>/` | `notes.views.approve_note` | Approve a note |
| `/notes/reject/<id>/` | `notes.views.reject_note` | Reject a note |
| `/notes/view/<id>/` | `notes.views.view_note` | Inline file viewer |
| `/notes/download/<id>/` | `notes.views.download_note` | Download file |
| `/admin/` | Django Admin | Built-in admin panel |

---

## 12. Screenshots & User Interface

### Design System
The UI uses a custom-built CSS design system (1300+ lines) with:
- **Color Palette:** Academic blue (#2563eb) as primary, steel slate neutrals, clean white surfaces
- **Typography:** Poppins font family from Google Fonts
- **Components:** Cards, pills, badges, buttons, dropdowns, forms, tables
- **Responsive:** Full mobile/tablet/desktop breakpoints

### Key Pages:
1. **Home Page** — Hero section with live stats, Engineering departments grid, About section, Trending notes preview, Features showcase, Stats banner, 3-column footer
2. **Dashboard** — Personal analytics cards, recent notes, bookmarks, subject exploration, community feed
3. **Browse Notes** — Multi-filter sidebar (search, subject, branch, semester, sort), note cards grid with bookmark/view buttons
4. **Note Detail** — Full content display, inline PDF/image preview, metadata sidebar, comments section, like/bookmark actions
5. **Upload Note** — Form with title, subject, branch, semester, description, file upload
6. **Create E-Note** — Rich text editor with whiteboard canvas for drawings
7. **My Notes** — Table view of all uploaded notes with status pills, action buttons
8. **Admin Dashboard** — All notes management with approve/reject actions, status filtering
9. **Login / Register** — Split-panel design with brand sidebar and form
10. **Profile** — View and edit personal information

---

## 13. Testing & Validation

### 13.1 Functional Testing

| Test Case | Expected Result | Status |
|-----------|----------------|--------|
| Register with valid data | User created, logged in, redirected to dashboard | ✅ Pass |
| Register with duplicate username | Error message "Username is already taken" | ✅ Pass |
| Register with mismatched passwords | Error message "Passwords do not match" | ✅ Pass |
| Login with valid credentials | Redirected to dashboard with welcome message | ✅ Pass |
| Login with invalid credentials | Error message displayed | ✅ Pass |
| Upload PDF note | Note saved with Pending status | ✅ Pass |
| Create online e-note | E-note saved with content and drawing data | ✅ Pass |
| Browse with search filter | Only matching notes displayed | ✅ Pass |
| View note detail | View counter increments by 1 | ✅ Pass |
| Bookmark/unbookmark note | Toggle works, reflected in bookmarks page | ✅ Pass |
| Like/unlike note | Like count updates correctly | ✅ Pass |
| Post comment | Comment appears on note detail page | ✅ Pass |
| Admin approve note | Status changes to Approved, visible in Browse | ✅ Pass |
| Admin reject note | Status changes to Rejected, hidden from Browse | ✅ Pass |
| Non-staff access admin dashboard | 403 Forbidden | ✅ Pass |
| Create user from Django shell | Profile auto-created by signal | ✅ Pass |

### 13.2 Database Verification

```sql
-- Verified in MySQL Workbench:
SELECT COUNT(*) FROM auth_user;          -- 4 users
SELECT COUNT(*) FROM accounts_profile;   -- 4 profiles (1:1 match)
SELECT COUNT(*) FROM notes_note;         -- All notes with correct status
SELECT COUNT(*) FROM notes_bookmark;     -- Bookmarks linked correctly
SELECT COUNT(*) FROM notes_comment;      -- Comments linked correctly
```

---

## 14. Future Scope

1. **AI-Powered Note Summarization** — Integrate OpenAI/Gemini API to auto-generate summaries of uploaded PDFs.
2. **Real-Time Chat** — WebSocket-based study group chat rooms per subject.
3. **Email Notifications** — Notify users when their notes are approved/rejected.
4. **Mobile App** — React Native or Flutter mobile application.
5. **OCR Integration** — Extract text from handwritten note images for searchability.
6. **Gamification** — Leaderboards, badges, and reward points for top contributors.
7. **Multi-Language Support** — Hindi and regional language translations.
8. **Cloud Deployment** — Deploy on AWS/GCP/Render with S3 for file storage.
9. **Analytics Dashboard** — Advanced charts showing upload trends, popular subjects, and user engagement metrics.
10. **Plagiarism Detection** — Check uploaded notes for duplicate content.

---

## 15. Conclusion

**StudyVerse** successfully demonstrates a full-stack web application built using the Django framework with MySQL database integration. The platform addresses a real-world problem faced by engineering students — the lack of a centralized, verified, and collaborative study material sharing system.

### Key Achievements:
- ✅ **Complete CRUD Operations** for notes with file upload and online e-note creation
- ✅ **Secure Authentication** with password hashing, CSRF protection, and session management
- ✅ **Admin Content Moderation** with 4-state workflow (Draft → Pending → Approved/Rejected)
- ✅ **Social Features** including bookmarks, likes, and comments
- ✅ **MySQL Production Database** managed via MySQL Workbench
- ✅ **Responsive UI Design** with custom CSS design system
- ✅ **Django Signals** for automatic profile creation across all user creation methods
- ✅ **Real-Time View Tracking** using atomic database operations
- ✅ **Multi-Branch & Semester Filtering** for targeted note discovery

The project demonstrates proficiency in **Python, Django, MySQL, HTML/CSS/JavaScript, Git**, and **software engineering principles** including separation of concerns, DRY (Don't Repeat Yourself), and the MVC/MVT design pattern.

---

*Report prepared by Ayush Kumar | July 2026*  
*StudyVerse — Empowering Minds, Sharing Knowledge*
