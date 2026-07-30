#!/usr/bin/env python3
"""
StudyVerse - Complete Fresh Project Report Generator (FPDF2)
Generates a comprehensive, professional, publication-quality PDF report for teacher presentation.
"""

import sys
import os
from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(100, 116, 139)
            self.cell(0, 8, 'StudyVerse - E-Notes Sharing Application | AWS Cloud Project Report', border=0, align='L')
            self.cell(0, 8, f'Page {self.page_no()}', border=0, align='R', new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(226, 232, 240)
            self.set_line_width(0.3)
            self.line(10, 15, 200, 15)
            self.ln(4)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(148, 163, 184)
            self.cell(0, 10, 'Lovely Professional University (LPU) - Department of Computer Science & Engineering', align='C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(30, 58, 138)  # Deep Navy Blue
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(37, 99, 235)  # Royal Blue Accent
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.set_line_width(0.2)
        self.ln(6)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(30, 41, 59)  # Slate 800
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(51, 65, 85)  # Slate 700
        self.multi_cell(0, 5.5, text)
        self.ln(3)

    def bullet(self, label, text=""):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(37, 99, 235)
        self.cell(6, 5.5, '-')
        if text:
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(30, 41, 59)
            self.cell(self.get_string_width(label) + 2, 5.5, label)
            self.set_font('Helvetica', '', 10)
            self.set_text_color(51, 65, 85)
            self.multi_cell(0, 5.5, f" {text}")
        else:
            self.set_font('Helvetica', '', 10)
            self.set_text_color(51, 65, 85)
            self.multi_cell(0, 5.5, label)
        self.ln(1.5)

    def add_table(self, headers, rows, col_widths=None):
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(241, 245, 249)  # Slate 100
        self.set_text_color(30, 41, 59)
        self.set_draw_color(203, 213, 225)
        
        if not col_widths:
            col_widths = [190 / len(headers)] * len(headers)

        # Header Row
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 7, header, border=1, align='C', fill=True)
        self.ln()

        # Data Rows
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(51, 65, 85)
        for r_idx, row in enumerate(rows):
            fill = (r_idx % 2 == 1)
            if fill:
                self.set_fill_color(248, 250, 252)
            else:
                self.set_fill_color(255, 255, 255)

            # Measure max height
            cell_heights = []
            for i, cell in enumerate(row):
                lines = self.multi_cell(col_widths[i], 4.5, str(cell), border=0, dry_run=True, output="LINES")
                cell_heights.append(len(lines) * 4.5 + 2)
            max_h = max(max_h for max_h in cell_heights if max_h > 0) if cell_heights else 6
            max_h = max(max_h, 6)

            for i, cell in enumerate(row):
                x = self.get_x()
                y = self.get_y()
                self.rect(x, y, col_widths[i], max_h, style='F' if fill else '')
                self.rect(x, y, col_widths[i], max_h)
                self.multi_cell(col_widths[i], 4.5, str(cell), border=0, align='L')
                self.set_xy(x + col_widths[i], y)
            self.ln(max_h)
        self.ln(4)

def build_pdf():
    pdf = PDFReport(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(10, 15, 10)

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    pdf.add_page()
    pdf.ln(12)
    
    # Title Box Header
    pdf.set_fill_color(30, 58, 138)  # Deep Navy
    pdf.rect(10, 25, 190, 42, style='F')
    
    pdf.set_font('Helvetica', 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 32)
    pdf.cell(190, 10, 'STUDYVERSE', align='C', new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(191, 219, 254)  # Light Blue
    pdf.cell(190, 8, 'Full-Stack E-Notes Sharing Platform & AWS Cloud Architecture', align='C', new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_xy(10, 75)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(190, 6, '"Empowering Minds, Sharing Knowledge"', align='C', new_x="LMARGIN", new_y="NEXT")

    pdf.ln(10)
    pdf.set_draw_color(37, 99, 235)
    pdf.set_line_width(1)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.set_line_width(0.2)
    pdf.ln(12)

    pdf.set_font('Helvetica', 'B', 15)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(190, 8, 'COMPREHENSIVE PROJECT REPORT', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(12)

    meta_details = [
        ('Project Title:', 'StudyVerse - E-Notes Sharing Application'),
        ('Student Name:', 'Ayush Kumar'),
        ('Registration / Roll:', 'LPU Engineering Student'),
        ('University:', 'Lovely Professional University (LPU)'),
        ('Course:', 'B.Tech Computer Science & Engineering'),
        ('Semester:', '7th Semester'),
        ('AWS EC2 Web App:', 'http://23.20.190.164'),
        ('AWS RDS MySQL:', 'dbstudyverse.c6nwkq8cuodu.us-east-1.rds.amazonaws.com'),
        ('AWS S3 Storage:', 'studyverse-uploads (us-east-1)'),
        ('Vercel Preview:', 'https://e-notes-sharing-application.vercel.app'),
        ('GitHub Repository:', 'github.com/Ayush12708/e-notes-sharing-application'),
        ('Submission Date:', 'July 2026'),
    ]

    for label, value in meta_details:
        pdf.set_font('Helvetica', 'B', 9.5)
        pdf.set_text_color(71, 85, 105)
        pdf.cell(48, 6.5, label, align='R')
        pdf.set_font('Helvetica', '', 9.5)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(0, 6.5, f'  {value}', new_x="LMARGIN", new_y="NEXT")

    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('Table of Contents')
    toc = [
        '1. Executive Summary & Project Introduction',
        '2. Problem Statement & Academic Motivation',
        '3. Project Objectives & Scope',
        '4. Cloud Infrastructure Architecture (AWS EC2, RDS, S3, Vercel)',
        '5. System Design & Django MVT Flow',
        '6. Database Schemas & Relational Data Model (MySQL)',
        '7. Core Modules & Feature Specifications',
        '8. User Interface & Single-Card Authentication Redesign',
        '9. Admin Content Moderation & Verification Workflow',
        '10. Interactive Whiteboard Canvas & E-Notes Studio',
        '11. URL Routing & API Structure',
        '12. Non-Functional Requirements & Security Protocols',
        '13. Testing, Verification & Benchmarking',
        '14. Teacher Presentation Viva Questions & Detailed Answers',
        '15. Future Scope & Conclusion',
    ]
    for item in toc:
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(30, 64, 175)
        pdf.cell(0, 7, f'    {item}', new_x="LMARGIN", new_y="NEXT")

    # =========================================================================
    # 1. EXECUTIVE SUMMARY & INTRODUCTION
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('1. Executive Summary & Project Introduction')
    pdf.body_text(
        'StudyVerse is a state-of-the-art, full-stack web application developed for university students and academic institutions. It provides a centralized, cloud-hosted platform where students can upload, create, search, bookmark, and discuss academic study notes, lecture slides, code cheat sheets, and exam preparation materials in real time.'
    )
    pdf.body_text(
        'Designed specifically to eliminate fragmented file sharing across social media chat groups, StudyVerse features automated moderation workflows, real-time analytics, interactive whiteboard drawing tools, and an enterprise cloud architecture built on AWS EC2, AWS RDS MySQL 8.0, and AWS S3 file storage.'
    )

    # =========================================================================
    # 2. PROBLEM STATEMENT & MOTIVATION
    # =========================================================================
    pdf.chapter_title('2. Problem Statement & Motivation')
    pdf.body_text(
        'In university environments, students encounter significant friction when attempting to access reliable study materials:'
    )
    pdf.bullet('Fragmented File Distribution', 'Notes are scattered across temporary WhatsApp groups, personal Google Drive folders, and chat links that expire over time.')
    pdf.bullet('Lack of Content Quality Verification', 'Materials uploaded informally often contain errors, missing chapters, or outdated syllabus topics without any peer or admin oversight.')
    pdf.bullet('No Subject or Semester Categorization', 'Finding specific subject notes for a given semester or branch requires manual searching through unstructured chat histories.')
    pdf.bullet('Zero Academic Discussion Context', 'Static file downloads offer no built-in mechanism for students to ask questions or discuss difficult concepts under a specific note.')

    # =========================================================================
    # 3. PROJECT OBJECTIVES & SCOPE
    # =========================================================================
    pdf.chapter_title('3. Project Objectives & Scope')
    pdf.body_text('The core engineering goals achieved in StudyVerse include:')
    objectives = [
        'Centralized Repository: Provide a single web destination for all university engineering branches and semesters.',
        'Rich E-Notes Studio & Whiteboard: Enable students to type formatted digital notes and draw hand-written diagrams using HTML5 Canvas.',
        'Multi-Format Support: Upload PDF, Word (.docx), PowerPoint (.pptx), Images (.png, .jpg), and ZIP archives.',
        'Admin Content Moderation: Ensure high quality via a 4-state lifecycle (Draft -> Pending -> Approved / Rejected) with live note preview.',
        'Enterprise AWS Cloud Hosting: Deploy web services on AWS EC2 (Ubuntu 24.04, Nginx 1.24, Gunicorn), production database on AWS RDS MySQL 8.0, and binary media assets on AWS S3.',
        'Atomic View Counter: Eliminate race conditions using Django F() expressions during concurrent view and download requests.',
    ]
    for obj in objectives:
        pdf.bullet(obj)

    # =========================================================================
    # 4. CLOUD INFRASTRUCTURE ARCHITECTURE
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('4. Cloud Infrastructure Architecture (AWS EC2, RDS, S3, Vercel)')
    pdf.body_text(
        'StudyVerse utilizes a multi-tier cloud infrastructure designed for high availability, zero data loss, and seamless scaling:'
    )

    cloud_table = [
        ['Layer', 'AWS / Cloud Service', 'Configuration Details & Specifications'],
        ['Virtual Server', 'AWS EC2 Instance', 'Ubuntu 24.04 LTS, Public IP 23.20.190.164, Nginx 1.24 Reverse Proxy, Gunicorn 26.0 WSGI Daemon'],
        ['Database Server', 'AWS RDS MySQL 8.0', 'dbstudyverse.c6nwkq8cuodu.us-east-1.rds.amazonaws.com (Port 3306, Schema: notehub_db)'],
        ['Media File Storage', 'AWS S3 Bucket', 'studyverse-uploads (us-east-1), django-storages + boto3 integration for PDF/DOCX/Image uploads'],
        ['Serverless Host', 'Vercel Serverless', 'e-notes-sharing-application.vercel.app (@vercel/python WSGI serverless builder)'],
        ['Static File Pipeline', 'WhiteNoise Storage', 'CompressedStaticFilesStorage serving minified CSS and JS directly via Gunicorn/Nginx'],
        ['Deployment Script', 'deploy_ec2.sh', 'Automated 1-command bash provisioning script installing Python virtualenv, system packages, & services'],
    ]
    pdf.add_table(cloud_table[0], cloud_table[1:], col_widths=[30, 50, 110])

    # =========================================================================
    # 5. SYSTEM DESIGN & DJANGO MVT FLOW
    # =========================================================================
    pdf.chapter_title('5. System Design & Django MVT Flow')
    pdf.body_text(
        'StudyVerse implements the Model-View-Template (MVT) design pattern:'
    )
    pdf.bullet('Model Layer (DB ORM)', 'Encapsulates User Profiles, Notes, Bookmarks, and Comments. Maps directly to AWS RDS MySQL tables.')
    pdf.bullet('View Layer (Business Logic)', 'Handles HTTP request dispatching, authentication checks, moderation state transitions, and S3 file streaming.')
    pdf.bullet('Template Layer (UI Rendering)', 'Renders responsive HTML5 components styled via a custom 1300+ line CSS design system.')
    pdf.bullet('Signal Dispatcher (accounts/signals.py)', 'Uses post_save signals on User model to guarantee Profile row creation regardless of user creation origin.')

    # =========================================================================
    # 6. DATABASE SCHEMAS & RELATIONAL DATA MODEL
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('6. Database Schemas & Relational Data Model (MySQL)')
    pdf.body_text('The relational database schema stored in AWS RDS MySQL 8.0 consists of the following primary tables:')

    db_table = [
        ['Table Name', 'Primary Fields & Data Types', 'Relationships & Constraints'],
        ['auth_user', 'id (INT PK), username (VARCHAR), email, password, is_staff, is_superuser', 'Core Django Auth table for multi-user logins'],
        ['accounts_profile', 'id (PK), user_id (FK), bio (TEXT), profile_picture, created_at', 'One-to-One linked to auth_user via Django Signals'],
        ['notes_note', 'id (PK), title, subject, branch, semester, file, status, views (INT), user_id (FK)', 'FK to auth_user; stores status (Pending/Approved/Rejected/Draft) & view counts'],
        ['notes_bookmark', 'id (PK), user_id (FK), note_id (FK), created_at', 'UniqueTogether constraint on (user, note) preventing duplicate bookmarks'],
        ['notes_comment', 'id (PK), note_id (FK), user_id (FK), content (TEXT), created_at', 'Foreign keys to notes_note and auth_user for discussion threads'],
    ]
    pdf.add_table(db_table[0], db_table[1:], col_widths=[35, 75, 80])

    # =========================================================================
    # 7. CORE MODULES & FEATURE SPECIFICATIONS
    # =========================================================================
    pdf.chapter_title('7. Core Modules & Feature Specifications')
    pdf.bullet('User Authentication & Profiles', 'Registration, login, logout, password updates, and single-card smooth UI.')
    pdf.bullet('Document Upload Studio', 'Supports uploading PDF, Word, PPTX, Images, and ZIP files directly to AWS S3.')
    pdf.bullet('Interactive Whiteboard E-Notes', 'HTML5 Canvas drawing studio with brush sizes, color palette, eraser, and save as draft.')
    pdf.bullet('Admin Content Moderation Panel', 'Status filter tabs (Pending, Approved, Rejected, Draft) and live note document preview modal.')
    pdf.bullet('Student Analytics Dashboard', 'Aggregates total notes submitted, approved notes, total views, and bookmarks.')

    # =========================================================================
    # 8. USER INTERFACE & SINGLE-CARD AUTHENTICATION REDESIGN
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('8. User Interface & Single-Card Authentication Redesign')
    pdf.body_text(
        'To elevate the user experience, the authentication pages were overhauled from split-screen layouts into a sober, centered single-card design:'
    )
    pdf.bullet('Centered Single-Card Container', 'Centered `.auth-card-single` layout eliminating visual distraction and side partitions.')
    pdf.bullet('Academic Color Palette', 'Ice slate background (`#f8fafc`), deep navy text (`#0f172a`), and subtle royal blue focus rings.')
    pdf.bullet('Two-Column Grid Fields', 'Structured form fields for First Name, Last Name, Branch, and Academic Year on registration.')

    # =========================================================================
    # 9. ADMIN CONTENT MODERATION & VERIFICATION WORKFLOW
    # =========================================================================
    pdf.chapter_title('9. Admin Content Moderation & Verification Workflow')
    pdf.body_text(
        'StudyVerse enforces quality control through a dedicated moderation dashboard (`/notes/admin-dashboard/`):'
    )
    pdf.bullet('Filter Tabs', 'View notes by status: All, Pending, Approved, Rejected, Draft.')
    pdf.bullet('Document Preview ([View Note])', 'Staff members can view note text or document contents before taking action.')
    pdf.bullet('Instant Approval / Rejection', 'Single-click action buttons update database status and make approved notes immediately visible to all students.')

    # =========================================================================
    # 10. URL ROUTING STRUCTURE
    # =========================================================================
    pdf.chapter_title('10. URL Routing Structure')
    urls_table = [
        ['URL Pattern', 'Handler View Function', 'Access Level & Description'],
        ['/', 'home.views.home', 'Public: Landing page with search & department grid'],
        ['/accounts/login/', 'accounts.views.login_view', 'Public: Single-card sober user login'],
        ['/accounts/register/', 'accounts.views.register_view', 'Public: User registration with signal auto-profile'],
        ['/dashboard/', 'dashboard.views.dashboard_view', 'Student: Personal metrics & uploaded notes list'],
        ['/notes/browse/', 'notes.views.browse_notes', 'Public/Student: Search & filter approved notes'],
        ['/notes/upload/', 'notes.views.upload_note', 'Student: Document file upload to AWS S3'],
        ['/notes/create-online/', 'notes.views.create_online_note', 'Student: Whiteboard canvas & e-notes studio'],
        ['/notes/admin-dashboard/', 'notes.views.admin_dashboard', 'Admin/Staff: Moderation panel with status tabs'],
    ]
    pdf.add_table(urls_table[0], urls_table[1:], col_widths=[45, 55, 90])

    # =========================================================================
    # 11. TEACHER PRESENTATION VIVA QUESTIONS & DETAILED ANSWERS
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('11. Teacher Presentation Viva Questions & Detailed Answers')
    pdf.body_text('This section provides comprehensive answers to expected viva voce questions for project evaluation:')

    viva_qna = [
        ('Q1: What is the overall architecture of StudyVerse?',
         'StudyVerse follows the Django MVT (Model-View-Template) architecture. It is deployed on an AWS EC2 instance running Ubuntu 24.04 with Nginx as a reverse proxy and Gunicorn as the WSGI server. Database storage is handled by AWS RDS MySQL 8.0, and media file uploads are stored in an AWS S3 bucket.'),
        
        ('Q2: How does the application handle high concurrent view counts without race conditions?',
         'View counting uses Django F() database expressions: `Note.objects.filter(id=pk).update(views=F("views") + 1)`. This executes the increment directly inside the MySQL database engine atomically, avoiding Python-level read-modify-write race conditions.'),
        
        ('Q3: How are User Profiles created automatically when a new User registers or is added via Admin/MySQL Workbench?',
         'We implemented Django Signals (`post_save`) in `accounts/signals.py`. Whenever a `User` instance is saved, the receiver function automatically instantiates an associated `Profile` record, ensuring 100% data integrity across all creation channels.'),
        
        ('Q4: What security measures protect user uploads and data in AWS S3 and RDS?',
         'AWS RDS is restricted via Security Groups on Port 3306. AWS S3 access keys (`boto3`) stream media uploads through signed bucket operations, while Django enforces CSRF tokens on all POST forms and hashed PBKDF2 passwords for user authentication.'),
        
        ('Q5: How does the Admin Moderation panel work?',
         'Notes submitted by students enter a `Pending` state. In `/notes/admin-dashboard/`, staff members can preview notes via the `[View Note]` modal, filter notes by status tabs, and click Approve or Reject, which updates the note status and toggles public visibility in the Browse Notes section.'),
    ]

    for q, a in viva_qna:
        pdf.section_title(q)
        pdf.body_text(a)
        pdf.ln(1)

    # =========================================================================
    # 12. CONCLUSION & FUTURE SCOPE
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title('12. Future Scope & Conclusion')
    pdf.body_text(
        'StudyVerse successfully bridges the gap in academic resource sharing by offering a reliable, admin-moderated, cloud-hosted platform. With its enterprise architecture on AWS EC2, RDS MySQL, and S3, it demonstrates industry-standard web engineering practices.'
    )
    pdf.section_title('Future Roadmap Improvements:')
    pdf.bullet('AI PDF Summarization', 'Integrate OpenAI / Gemini API to auto-generate 1-paragraph summary guides for uploaded notes.')
    pdf.bullet('Mobile Application', 'Develop React Native mobile app utilizing Django REST Framework endpoints.')
    pdf.bullet('Elasticsearch Integration', 'Full-text OCR indexing inside uploaded PDF documents for instant deep keyword search.')

    pdf.ln(10)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(30, 58, 138)
    pdf.cell(0, 8, 'Report Generated Successfully for Presentation & Academic Evaluation.', align='C')

    output_path = '/Users/ayushkumar/Desktop/NoteHub/StudyVerse_Project_Report.pdf'
    pdf.output(output_path)
    print(f"✅ Complete fresh PDF report created at: {output_path}")

if __name__ == '__main__':
    build_pdf()
