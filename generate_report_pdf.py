#!/usr/bin/env python3
"""Generate a professional PDF project report for StudyVerse using fpdf2."""
from fpdf import FPDF
import os

class ProjectReport(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(100, 116, 139)
            self.cell(0, 8, 'StudyVerse - E-Notes Sharing Application | Project Report', align='L')
            self.cell(0, 8, f'Page {self.page_no()}', align='R', new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(226, 232, 240)
            self.line(15, 16, 195, 16)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, 'Prepared by Ayush Kumar | Lovely Professional University | July 2026', align='C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(30, 64, 175)
        self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(37, 99, 235)
        self.set_line_width(0.6)
        self.line(15, self.get_y(), 195, self.get_y())
        self.set_line_width(0.2)
        self.ln(6)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(30, 58, 138)
        self.ln(3)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(226, 232, 240)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(4)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 5.5, f'- {text}')
        self.ln(1)

    def bold_bullet(self, bold_text, normal_text):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(30, 41, 59)
        self.write(5.5, f'- {bold_text} ')
        self.set_font('Helvetica', '', 10)
        self.write(5.5, f'{normal_text}\n')
        self.ln(2)

    def add_table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [180 / len(headers)] * len(headers)

        # Header
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(30, 64, 175)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 8, h, border=1, fill=True, align='C')
        self.ln()

        # Rows
        self.set_font('Helvetica', '', 9)
        self.set_text_color(30, 41, 59)
        fill = False
        for row in rows:
            if fill:
                self.set_fill_color(248, 250, 252)
            else:
                self.set_fill_color(255, 255, 255)

            max_h = 8
            for i, cell in enumerate(row):
                lines = self.multi_cell(col_widths[i], 5, str(cell), border=0, split_only=True)
                h = max(len(lines) * 5, 8)
                if h > max_h:
                    max_h = h

            x_start = self.get_x()
            y_start = self.get_y()

            # Check page break
            if y_start + max_h > self.page_break_trigger:
                self.add_page()
                y_start = self.get_y()

            for i, cell in enumerate(row):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                self.multi_cell(col_widths[i], 5, str(cell), border=1, fill=True)

            self.set_y(y_start + max_h)
            fill = not fill
        self.ln(4)


# Create PDF
pdf = ProjectReport()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.set_margins(15, 15, 15)

# COVER PAGE
pdf.add_page()
pdf.ln(25)
pdf.set_font('Helvetica', 'B', 30)
pdf.set_text_color(30, 64, 175)
pdf.cell(0, 16, 'StudyVerse', align='C', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('Helvetica', '', 13)
pdf.set_text_color(100, 116, 139)
pdf.cell(0, 8, 'E-Notes Sharing Application', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 8, '"Empowering Minds, Sharing Knowledge"', align='C', new_x="LMARGIN", new_y="NEXT")

pdf.ln(6)
pdf.set_draw_color(37, 99, 235)
pdf.set_line_width(1)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.set_line_width(0.2)
pdf.ln(10)

pdf.set_font('Helvetica', 'B', 15)
pdf.set_text_color(30, 41, 59)
pdf.cell(0, 10, 'DETAILED PROJECT REPORT', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.ln(15)

details = [
    ('Project Title:', 'StudyVerse - E-Notes Sharing Application'),
    ('Developed By:', 'Ayush Kumar'),
    ('University:', 'Lovely Professional University (LPU)'),
    ('Course:', 'B.Tech Computer Science Engineering'),
    ('Semester:', '7th Semester'),
    ('GitHub:', 'github.com/Ayush12708/e-notes-sharing-application'),
    ('Date:', 'July 2026'),
]

for label, value in details:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(45, 8, label, align='R')
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 8, f'  {value}', new_x="LMARGIN", new_y="NEXT")

# TABLE OF CONTENTS
pdf.add_page()
pdf.chapter_title('Table of Contents')
toc_items = [
    '1. Introduction',
    '2. Problem Statement',
    '3. Objectives',
    '4. Technology Stack',
    '5. System Architecture',
    '6. Database Design (ER Diagram & Schema)',
    '7. Module Description',
    '8. Functional Requirements',
    '9. Non-Functional Requirements',
    '10. Implementation Details',
    '11. URL Routing Structure',
    '12. Screenshots & User Interface',
    '13. Testing & Validation',
    '14. Future Scope',
    '15. Conclusion',
]
for item in toc_items:
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(30, 64, 175)
    pdf.cell(0, 8, f'    {item}', new_x="LMARGIN", new_y="NEXT")

# 1. INTRODUCTION
pdf.add_page()
pdf.chapter_title('1. Introduction')
pdf.body_text(
    'StudyVerse is a full-stack web-based E-Notes Sharing Application designed to allow college and university students to upload, share, browse, and manage academic study materials such as lecture notes, PDF documents, and digitally-created e-notes. The platform enables peer-to-peer knowledge exchange across multiple engineering branches and semesters with features like bookmarking, commenting, likes, admin content moderation, and real-time view tracking.'
)
pdf.body_text(
    'The application follows the Django MVT (Model-View-Template) architectural pattern and uses MySQL as its production database managed via MySQL Workbench, making it a robust, scalable, and secure platform for academic collaboration.'
)
pdf.body_text('Tagline: "Empowering Minds, Sharing Knowledge"')

# 2. PROBLEM STATEMENT
pdf.chapter_title('2. Problem Statement')
pdf.body_text('College students often face significant challenges in accessing quality study materials:')
problems = [
    ('Fragmented Resources:', 'Notes are scattered across WhatsApp groups, Google Drive links, and personal devices with no centralized access point.'),
    ('No Quality Control:', 'Shared materials often lack verification, leading to incorrect or incomplete content.'),
    ('Limited Discovery:', 'Students struggle to find notes for specific subjects, semesters, or branches.'),
    ('No Collaboration:', 'Traditional file sharing provides no mechanism for discussions or feedback.'),
    ('Loss of Materials:', 'Students frequently lose access when WhatsApp groups are deleted or Drive links expire.'),
]
for b, t in problems:
    pdf.bold_bullet(b, t)
pdf.body_text('StudyVerse solves these problems by providing a permanent, centralized, admin-verified platform where students can upload, discover, bookmark, and discuss study materials with real-time analytics.')

# 3. OBJECTIVES
pdf.chapter_title('3. Objectives')
objectives = [
    'Build a centralized platform where students from any branch can upload and access notes.',
    'Support file uploads (PDF, DOCX, PPTX, images) and online rich-text e-note creation with whiteboard drawing canvas.',
    'Implement admin content moderation workflow (Pending -> Approved / Rejected).',
    'Enable smart search and filtering by subject, branch, semester, keyword, and sorting.',
    'Allow users to like, bookmark, and comment on notes for academic discussion.',
    'Track real-time note view counts and display live statistics.',
    'Provide secure multi-user authentication with concurrent session handling.',
    'Store all data in MySQL database managed via MySQL Workbench.',
]
for i, obj in enumerate(objectives, 1):
    pdf.body_text(f'{i}. {obj}')

# 4. TECHNOLOGY STACK
pdf.add_page()
pdf.chapter_title('4. Technology Stack')
pdf.add_table(
    ['Layer', 'Technology', 'Purpose'],
    [
        ['Backend', 'Django 5.x (Python)', 'Server-side logic, ORM, auth'],
        ['Frontend', 'HTML5, CSS3, JavaScript', 'Templates, responsive UI'],
        ['Database', 'MySQL 8.0 (Workbench)', 'Production data storage'],
        ['MySQL Driver', 'PyMySQL', 'Python-MySQL interface'],
        ['CSS', 'Custom Design System', '1300+ lines hand-crafted CSS'],
        ['Fonts', 'Google Fonts (Poppins)', 'Modern typography'],
        ['Version Control', 'Git + GitHub', 'Source code management'],
        ['Deployment', 'Gunicorn + WhiteNoise', 'WSGI server + static files'],
    ],
    col_widths=[35, 55, 90]
)

pdf.section_title('Python Dependencies')
pdf.body_text('requirements.txt: django, gunicorn, whitenoise, pymysql')

# 5. SYSTEM ARCHITECTURE
pdf.chapter_title('5. System Architecture')
pdf.section_title('5.1 Django MVT Flow')
pdf.body_text('Client (Browser) -> URL Dispatcher (config/urls.py) -> Views (accounts, notes, dashboard, home) -> Models (ORM queries to MySQL) + Templates (HTML rendering) -> HTTP Response back to Client')
pdf.ln(2)

pdf.section_title('5.2 Project Directory Structure')
dirs = [
    'config/          - Project settings, URLs, WSGI',
    'accounts/        - User auth: models, views, forms, signals, admin',
    'notes/           - Core CRUD: models, views, forms, URLs',
    'dashboard/       - Student dashboard: views, URLs',
    'home/            - Landing page: views, URLs',
    'templates/       - HTML templates (base, accounts, notes, dashboard)',
    'static/css/      - Custom CSS design system (1300+ lines)',
    'static/js/       - Client-side JavaScript',
    'media/notes/     - Uploaded note files (PDF, DOCX, etc.)',
]
for d in dirs:
    pdf.bullet(d)

# 6. DATABASE DESIGN
pdf.add_page()
pdf.chapter_title('6. Database Design')
pdf.section_title('6.1 ER Relationships')
pdf.body_text('auth_user (1) ----> (1) accounts_profile    [One-to-One]')
pdf.body_text('auth_user (1) ----> (N) notes_note           [One-to-Many]')
pdf.body_text('notes_note (1) ---> (N) notes_bookmark       [One-to-Many]')
pdf.body_text('notes_note (1) ---> (N) notes_comment        [One-to-Many]')
pdf.body_text('notes_note (N) <--> (N) auth_user via notes_note_likes  [Many-to-Many]')
pdf.ln(2)

pdf.section_title('6.2 MySQL Table Schema')
pdf.add_table(
    ['Table Name', 'Key Fields', 'Description'],
    [
        ['auth_user', 'id, username, password, email, is_staff', 'Django built-in user auth table'],
        ['accounts_profile', 'user_id (FK), phone, college, semester', 'Extended profile (1:1 with User)'],
        ['notes_note', 'title, subject, branch, semester, content, file, status, views', 'Core notes table'],
        ['notes_bookmark', 'user_id (FK), note_id (FK), created_at', 'Saved bookmarks'],
        ['notes_comment', 'note_id (FK), user_id (FK), text', 'Discussion comments'],
        ['notes_note_likes', 'note_id (FK), user_id (FK)', 'Many-to-many likes'],
        ['django_session', 'session_key, session_data, expire_date', 'Active login sessions'],
    ],
    col_widths=[42, 75, 63]
)

# 7. MODULE DESCRIPTION
pdf.add_page()
pdf.chapter_title('7. Module Description')

pdf.section_title('Module 1: Accounts (Authentication & Profile)')
features_auth = [
    ('Registration:', 'Users register with username, email, password, phone, college, semester. Passwords hashed with PBKDF2.'),
    ('Login:', 'Case-insensitive username matching. Supports redirect after login (?next= parameter).'),
    ('Profile:', 'View and edit personal details. Auto-created via Django signals for all user creation methods.'),
    ('Admin:', 'Profile displayed inline in Django Admin User page.'),
]
for b, t in features_auth:
    pdf.bold_bullet(b, t)

pdf.section_title('Module 2: Notes (Core CRUD & Content)')
features_notes = [
    ('Upload File Note:', 'Upload PDF, DOCX, PPTX, images with metadata (title, subject, branch, semester).'),
    ('Create Online E-Note:', 'Rich-text editor with whiteboard drawing canvas for diagrams.'),
    ('Browse Notes:', 'Multi-filter search by subject, branch, semester, keyword. Sorting by newest, oldest, A-Z, popular.'),
    ('Note Detail:', 'Full display with inline PDF/image preview, view counter, likes, bookmarks, comments.'),
    ('Real-Time Views:', 'Atomic F() expression increments view count on every page load.'),
    ('Edit/Delete:', 'Authors can modify or remove their own notes.'),
    ('Draft System:', 'Save notes as Draft without submitting for review.'),
]
for b, t in features_notes:
    pdf.bold_bullet(b, t)

pdf.section_title('Module 3: Social Engagement')
features_social = [
    ('Bookmarks:', 'Toggle save/unsave on any note. AJAX-powered. Dedicated bookmarks page.'),
    ('Likes:', 'Toggle like/unlike. AJAX response returns updated count.'),
    ('Comments:', 'Post discussion comments on note detail page. Ordered by newest.'),
]
for b, t in features_social:
    pdf.bold_bullet(b, t)

pdf.section_title('Module 4: Admin Content Moderation')
pdf.body_text('Staff-only Admin Dashboard showing all notes with Pending/Approved/Rejected counts. Admin can approve or reject any note. 4-state workflow: Draft -> Pending -> Approved / Rejected. Only approved notes visible in Browse.')

pdf.section_title('Module 5: Dashboard (Student Analytics)')
pdf.body_text('Personal stats (total notes, approved, pending, downloads, likes), recent notes, bookmarks, subject exploration with live counts, and community feed.')

pdf.section_title('Module 6: Home (Landing Page)')
pdf.body_text('Hero section with live stats, Engineering Departments grid, About section with 3-step workflow, Trending Notes preview, Features showcase, Stats banner, and 3-column footer.')

# 8. FUNCTIONAL REQUIREMENTS
pdf.add_page()
pdf.chapter_title('8. Functional Requirements')
pdf.add_table(
    ['ID', 'Requirement', 'Status'],
    [
        ['FR-01', 'Register with username, email, password, phone, college, semester', 'Done'],
        ['FR-02', 'Login with username and password (case-insensitive)', 'Done'],
        ['FR-03', 'View and update profile information', 'Done'],
        ['FR-04', 'Upload notes as PDF/DOCX/PPTX/Image files', 'Done'],
        ['FR-05', 'Create online e-notes with rich text and whiteboard', 'Done'],
        ['FR-06', 'Browse notes with search, filter, and sort', 'Done'],
        ['FR-07', 'View full note details with inline file preview', 'Done'],
        ['FR-08', 'Real-time view counter on note open', 'Done'],
        ['FR-09', 'Bookmark/unbookmark notes', 'Done'],
        ['FR-10', 'Like/unlike notes', 'Done'],
        ['FR-11', 'Post comments on notes', 'Done'],
        ['FR-12', 'Edit/delete own notes', 'Done'],
        ['FR-13', 'Save notes as Draft', 'Done'],
        ['FR-14', 'Admin dashboard to view all notes', 'Done'],
        ['FR-15', 'Admin approve/reject pending notes', 'Done'],
        ['FR-16', 'All data stored in MySQL via Workbench', 'Done'],
        ['FR-17', 'Auto-create Profile for users created by any method', 'Done'],
    ],
    col_widths=[15, 130, 35]
)

# 9. NON-FUNCTIONAL REQUIREMENTS
pdf.chapter_title('9. Non-Functional Requirements')
pdf.add_table(
    ['Requirement', 'Implementation'],
    [
        ['Security', 'PBKDF2_SHA256 password hashing, CSRF protection, @login_required decorators, @staff_member_required'],
        ['Performance', 'Django F() atomic updates, lazy QuerySet, select_related() for JOIN optimization'],
        ['Scalability', 'MySQL production DB, concurrent sessions, Gunicorn multi-worker WSGI'],
        ['Responsiveness', 'Fully responsive CSS with breakpoints at 992px and 640px'],
        ['Usability', 'Clean academic blue palette, flash messages, intuitive navigation'],
    ],
    col_widths=[40, 140]
)

# 10. IMPLEMENTATION DETAILS
pdf.add_page()
pdf.chapter_title('10. Implementation Details')

pdf.section_title('10.1 User Registration Flow')
pdf.body_text('1. User fills registration form (username, email, password, phone, college, semester)')
pdf.body_text('2. Form validated (password match, unique username check)')
pdf.body_text('3. User.objects.create_user() creates entry in auth_user with hashed password')
pdf.body_text('4. Profile.objects.create() creates entry in accounts_profile')
pdf.body_text('5. User is automatically logged in via login(request, user)')
pdf.body_text('6. Redirected to Dashboard with success message')

pdf.section_title('10.2 Django Signal for Auto-Profile')
pdf.body_text('A post_save signal on the User model automatically creates a Profile record whenever a new User is created - whether via website registration, Django admin, manage.py createsuperuser, Django shell, or any backend script.')

pdf.section_title('10.3 Real-Time View Counter')
pdf.body_text('Uses Django F() expression: Note.objects.filter(pk=pk).update(views=F("views") + 1). This generates atomic SQL: UPDATE notes_note SET views = views + 1, preventing race conditions with concurrent users.')

pdf.section_title('10.4 MySQL Connection')
pdf.body_text('PyMySQL is installed as MySQLdb compatible driver. settings.py configures ENGINE=django.db.backends.mysql connecting to notehub_db on localhost:3306.')

pdf.section_title('10.5 Content Moderation Workflow')
pdf.body_text('User uploads note -> Status = "Pending" -> Admin reviews in Dashboard -> Approved (visible in Browse) or Rejected (hidden). Users can also save as "Draft" for later editing.')

# 11. URL ROUTING
pdf.add_page()
pdf.chapter_title('11. URL Routing Structure')
pdf.add_table(
    ['URL Pattern', 'View', 'Description'],
    [
        ['/', 'home', 'Landing page'],
        ['/accounts/register/', 'register', 'User registration'],
        ['/accounts/login/', 'login_view', 'User login'],
        ['/accounts/logout/', 'logout_view', 'User logout'],
        ['/accounts/profile/', 'profile_view', 'View/edit profile'],
        ['/dashboard/', 'dashboard', 'Student dashboard'],
        ['/notes/upload/', 'upload_note', 'Upload file note'],
        ['/notes/create-online/', 'create_online_note', 'Create e-note'],
        ['/notes/browse/', 'browse_notes', 'Browse & search notes'],
        ['/notes/detail/<id>/', 'note_detail', 'View note details'],
        ['/notes/my-notes/', 'my_notes', 'User uploaded notes'],
        ['/notes/edit/<id>/', 'edit_note', 'Edit own note'],
        ['/notes/delete/<id>/', 'delete_note', 'Delete own note'],
        ['/notes/bookmark/<id>/', 'toggle_bookmark', 'Save/unsave bookmark'],
        ['/notes/like/<id>/', 'toggle_like', 'Like/unlike note'],
        ['/notes/bookmarks/', 'bookmarks_list', 'View saved bookmarks'],
        ['/notes/admin-dashboard/', 'admin_dashboard', 'Admin moderation'],
        ['/notes/approve/<id>/', 'approve_note', 'Approve a note'],
        ['/notes/reject/<id>/', 'reject_note', 'Reject a note'],
        ['/admin/', 'Django Admin', 'Built-in admin panel'],
    ],
    col_widths=[55, 45, 80]
)

# 12. UI DESIGN
pdf.chapter_title('12. Screenshots & User Interface')
pdf.body_text('The UI uses a custom-built CSS design system (1300+ lines) with:')
pdf.bullet('Color Palette: Academic blue (#2563eb) primary, steel slate neutrals, clean white surfaces')
pdf.bullet('Typography: Poppins font family from Google Fonts')
pdf.bullet('Components: Cards, pills, badges, buttons, dropdowns, forms, tables, department grids')
pdf.bullet('Responsive: Full mobile/tablet/desktop breakpoints at 992px and 640px')
pdf.ln(2)
pdf.body_text('Key Pages: Home (hero + departments + about + trending + features + stats + footer), Dashboard, Browse Notes, Note Detail, Upload Note, Create E-Note, My Notes, Admin Dashboard, Login/Register, Profile.')

# 13. TESTING
pdf.add_page()
pdf.chapter_title('13. Testing & Validation')
pdf.add_table(
    ['Test Case', 'Expected Result', 'Status'],
    [
        ['Register with valid data', 'User created, logged in, redirected', 'Pass'],
        ['Register duplicate username', 'Error "Username taken"', 'Pass'],
        ['Register password mismatch', 'Error "Passwords do not match"', 'Pass'],
        ['Login valid credentials', 'Redirect to dashboard', 'Pass'],
        ['Login invalid credentials', 'Error message displayed', 'Pass'],
        ['Upload PDF note', 'Saved with Pending status', 'Pass'],
        ['Create online e-note', 'Saved with content + drawing data', 'Pass'],
        ['Browse with search filter', 'Only matching notes shown', 'Pass'],
        ['View note detail', 'View counter increments by 1', 'Pass'],
        ['Bookmark/unbookmark', 'Toggle works correctly', 'Pass'],
        ['Like/unlike note', 'Count updates correctly', 'Pass'],
        ['Post comment', 'Comment appears on detail page', 'Pass'],
        ['Admin approve note', 'Status -> Approved, visible in Browse', 'Pass'],
        ['Admin reject note', 'Status -> Rejected, hidden', 'Pass'],
        ['Non-staff access admin panel', '403 Forbidden', 'Pass'],
        ['Create user from Django shell', 'Profile auto-created by signal', 'Pass'],
    ],
    col_widths=[60, 75, 45]
)

# 14. FUTURE SCOPE
pdf.chapter_title('14. Future Scope')
future = [
    'AI-Powered Note Summarization using OpenAI/Gemini API',
    'Real-Time Chat via WebSocket study group rooms',
    'Email Notifications for note approval/rejection',
    'Mobile App using React Native or Flutter',
    'OCR Integration to extract text from handwritten notes',
    'Gamification with leaderboards, badges, and reward points',
    'Multi-Language Support (Hindi and regional languages)',
    'Cloud Deployment on AWS/GCP with S3 file storage',
    'Advanced Analytics with charts for upload trends and engagement',
    'Plagiarism Detection for uploaded content',
]
for i, item in enumerate(future, 1):
    pdf.body_text(f'{i}. {item}')

# 15. CONCLUSION
pdf.add_page()
pdf.chapter_title('15. Conclusion')
pdf.body_text(
    'StudyVerse successfully demonstrates a full-stack web application built using the Django framework with MySQL database integration. The platform addresses a real-world problem faced by engineering students - the lack of a centralized, verified, and collaborative study material sharing system.'
)
pdf.ln(4)
pdf.section_title('Key Achievements')
achievements = [
    'Complete CRUD Operations for notes with file upload and online e-note creation',
    'Secure Authentication with password hashing, CSRF protection, and session management',
    'Admin Content Moderation with 4-state workflow (Draft -> Pending -> Approved/Rejected)',
    'Social Features including bookmarks, likes, and comments',
    'MySQL Production Database managed via MySQL Workbench',
    'Responsive UI Design with custom CSS design system (1300+ lines)',
    'Django Signals for automatic profile creation across all user creation methods',
    'Real-Time View Tracking using atomic database operations',
    'Multi-Branch & Semester Filtering for targeted note discovery',
]
for a in achievements:
    pdf.bullet(a)

pdf.ln(8)
pdf.set_draw_color(37, 99, 235)
pdf.set_line_width(0.8)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.set_line_width(0.2)
pdf.ln(6)

pdf.set_font('Helvetica', 'I', 10)
pdf.set_text_color(100, 116, 139)
pdf.cell(0, 6, 'The project demonstrates proficiency in Python, Django, MySQL, HTML/CSS/JS, Git,', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, 'and software engineering principles including MVC/MVT design pattern.', align='C', new_x="LMARGIN", new_y="NEXT")

pdf.ln(10)
pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(30, 64, 175)
pdf.cell(0, 8, 'StudyVerse - Empowering Minds, Sharing Knowledge', align='C', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(100, 116, 139)
pdf.cell(0, 8, 'Report prepared by Ayush Kumar | July 2026', align='C')

# Save PDF
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'StudyVerse_Project_Report.pdf')
pdf.output(output_path)
print(f'✅ PDF generated successfully: {output_path}')
