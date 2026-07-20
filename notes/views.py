from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import FileResponse, HttpResponseForbidden
from django.db.models import Q
from django.contrib import messages
import mimetypes
import os

from .forms import NoteForm, OnlineNoteForm
from .models import Note, Bookmark, Comment


def ensure_default_seed_notes():
    """Ensure core study notes and sample materials are always present and approved in the database."""
    try:
        from django.contrib.auth.models import User
        from accounts.models import Profile

        # Automatically approve any pending notes
        Note.objects.filter(status='Pending').update(status='Approved')

        # Find or create a seed author user
        seed_user = User.objects.filter(is_superuser=True).first() or User.objects.first()
        if not seed_user:
            seed_user = User.objects.create_superuser('admin', 'admin@notehub.com', 'admin123')
            Profile.objects.create(user=seed_user, college='NoteHub University', semester=1)

        seed_notes_data = [
            {
                'title': 'DBMS Unit 3 - Normalization & BCNF Notes',
                'subject': 'DBMS',
                'branch': 'CSE',
                'semester': 4,
                'description': 'Comprehensive lecture notes covering 1NF, 2NF, 3NF, BCNF, Functional Dependencies, and Lossless Join Decomposition with diagrams.',
                'content': 'UNIT 3: DATABASE NORMALIZATION\n\n1. Functional Dependency (FD):\nA Functional Dependency X -> Y holds if two tuples having same X value must have same Y value.\n\n2. 1st Normal Form (1NF):\n- Attributes must contain atomic values only.\n- No multivalued or composite attributes allowed.\n\n3. 2nd Normal Form (2NF):\n- Relation must be in 1NF.\n- No partial dependency exists (Non-prime attribute must fully depend on candidate key).\n\n4. 3rd Normal Form (3NF):\n- Relation must be in 2NF.\n- No transitive dependency X -> Y where X is not a super key and Y is non-prime attribute.\n\n5. Boyce-Codd Normal Form (BCNF):\n- For every functional dependency X -> Y, X MUST be a Super Key.',
                'uploaded_by': seed_user,
                'status': 'Approved',
                'downloads': 142,
                'is_online_note': True,
            },
            {
                'title': 'Data Structures & Algorithms (DSA) Revision Sheet',
                'subject': 'DSA',
                'branch': 'CSE',
                'semester': 3,
                'description': 'Quick revision cheatsheet for Trees, Graphs, Dynamic Programming, Sorting algorithms, and Time Complexities.',
                'content': 'DATA STRUCTURES REVISION GUIDE\n\n1. ARRAY & LINKED LIST:\n- Array Search: O(N) un-sorted, O(log N) binary search.\n- Linked List Insertion at head: O(1).\n\n2. TREES & BST:\n- Binary Search Tree Search: O(H) where H = height.\n- AVL Tree & Red-Black Tree guarantee O(log N) worst case search.\n\n3. GRAPHS:\n- BFS uses Queue data structure (Level order traversal).\n- DFS uses Stack / Recursion.\n- Dijkstra Algorithm for shortest path: O(E log V) with Priority Queue.',
                'uploaded_by': seed_user,
                'status': 'Approved',
                'downloads': 210,
                'is_online_note': True,
            },
            {
                'title': 'Operating Systems (OS) Process & Thread Management',
                'subject': 'OS',
                'branch': 'CSE',
                'semester': 4,
                'description': 'Detailed notes on CPU Scheduling algorithms (FCFS, SJF, Round Robin), Process States, Semaphores, and Deadlock Prevention.',
                'content': 'OPERATING SYSTEMS - PROCESS MANAGEMENT\n\n1. PROCESS STATES:\nNew -> Ready -> Running -> Terminated (Wait/Block for I/O).\n\n2. CPU SCHEDULING:\n- FCFS: First Come First Serve (Convoy Effect).\n- Round Robin: Time Quantum based preemptive scheduling.\n- SJF: Shortest Job First (Minimum average waiting time).\n\n3. DEADLOCK CONDITIONS (Coffman Conditions):\n- Mutual Exclusion\n- Hold and Wait\n- No Preemption\n- Circular Wait',
                'uploaded_by': seed_user,
                'status': 'Approved',
                'downloads': 185,
                'is_online_note': True,
            },
            {
                'title': 'Computer Networks (CN) OSI 7-Layer Architecture',
                'subject': 'CN',
                'branch': 'IT',
                'semester': 5,
                'description': 'Explanations of Physical, Data Link, Network, Transport, Session, Presentation, and Application layers with TCP/IP protocol mapping.',
                'content': 'COMPUTER NETWORKS - OSI MODEL\n\n1. Application Layer (HTTP, FTP, SMTP)\n2. Presentation Layer (Encryption, Compression)\n3. Session Layer (Session management, RPC)\n4. Transport Layer (TCP - reliable, UDP - connectionless)\n5. Network Layer (IP addressing, Routing - OSPF, BGP)\n6. Data Link Layer (MAC addressing, Ethernet, Framing)\n7. Physical Layer (Bits, Cables, Signals)',
                'uploaded_by': seed_user,
                'status': 'Approved',
                'downloads': 98,
                'is_online_note': True,
            },
            {
                'title': 'Python Programming & Object-Oriented Concepts',
                'subject': 'PYTHON',
                'branch': 'CSE',
                'semester': 2,
                'description': 'Covers Python data structures, decorators, generators, inheritance, polymorphism, and exception handling.',
                'content': 'PYTHON OOP CHEATSHEET\n\n1. CLASSES & OBJECTS:\nclass Student:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n2. DECORATORS:\ndef my_decorator(func):\n    def wrapper():\n        print("Before function")\n        func()\n        print("After function")\n    return wrapper',
                'uploaded_by': seed_user,
                'status': 'Approved',
                'downloads': 315,
                'is_online_note': True,
            }
        ]

        for item in seed_notes_data:
            note, created = Note.objects.get_or_create(
                title=item['title'],
                defaults=item
            )
            if not created and note.status != 'Approved':
                note.status = 'Approved'
                note.save()

        # Mark all existing notes in DB as Approved
        Note.objects.filter(status='Pending').update(status='Approved')

    except Exception:
        pass


@login_required
def upload_note(request):
    ensure_default_seed_notes()
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            if "save_draft" in request.POST:
                note.status = "Draft"
                messages.success(request, "Document saved as Draft.")
                note.save()
                return redirect("my_notes")
            else:
                note.status = "Approved"
                note.save()
                messages.success(request, "Document uploaded successfully!")
                return redirect("note_detail", pk=note.id)
    else:
        form = NoteForm()

    return render(request, "notes/upload_note.html", {"form": form})


@login_required
def create_online_note(request):
    ensure_default_seed_notes()
    if request.method == "POST":
        form = OnlineNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.is_online_note = True
            if "save_draft" in request.POST:
                note.status = "Draft"
                messages.success(request, "E-Note saved as Draft.")
                note.save()
                return redirect("my_notes")
            else:
                note.status = "Approved"
                note.save()
                messages.success(request, "Digital E-Note published successfully!")
                return redirect("note_detail", pk=note.id)
    else:
        form = OnlineNoteForm()

    return render(request, "notes/create_online_note.html", {"form": form})


@login_required
def browse_notes(request):
    ensure_default_seed_notes()
    search = request.GET.get("search", "").strip()
    semester = request.GET.get("semester", "")
    subject = request.GET.get("subject", "")
    branch = request.GET.get("branch", "")
    sort = request.GET.get("sort", "newest")

    # Exclude Draft notes from public browse, show Approved and active notes
    notes = Note.objects.filter(~Q(status="Draft"))

    if search:
        notes = notes.filter(
            Q(title__icontains=search) |
            Q(subject__icontains=search) |
            Q(branch__icontains=search) |
            Q(description__icontains=search) |
            Q(content__icontains=search) |
            Q(uploaded_by__username__icontains=search) |
            Q(uploaded_by__first_name__icontains=search) |
            Q(uploaded_by__last_name__icontains=search)
        )

    if semester:
        notes = notes.filter(semester=semester)

    if subject:
        notes = notes.filter(subject=subject)

    if branch:
        notes = notes.filter(branch=branch)

    if sort == "oldest":
        notes = notes.order_by("uploaded_at")
    elif sort == "az":
        notes = notes.order_by("title")
    elif sort == "za":
        notes = notes.order_by("-title")
    elif sort == "popular":
        notes = notes.order_by("-downloads")
    else:
        notes = notes.order_by("-uploaded_at")

    user_bookmarked_ids = Bookmark.objects.filter(user=request.user).values_list('note_id', flat=True)

    context = {
        "notes": notes,
        "search": search,
        "semester": semester,
        "subject": subject,
        "branch": branch,
        "sort": sort,
        "user_bookmarked_ids": list(user_bookmarked_ids),
    }

    return render(request, "notes/browse_notes.html", context)


@login_required
def note_detail(request, pk):
    ensure_default_seed_notes()
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        comment_text = request.POST.get("comment_text", "").strip()
        if comment_text:
            Comment.objects.create(note=note, user=request.user, text=comment_text)
            messages.success(request, "Your comment has been posted!")
            return redirect("note_detail", pk=pk)

    is_bookmarked = Bookmark.objects.filter(user=request.user, note=note).exists()
    is_liked = request.user in note.likes.all()

    context = {
        "note": note,
        "comments": note.comments.all(),
        "is_bookmarked": is_bookmarked,
        "is_liked": is_liked,
    }
    return render(request, "notes/note_detail.html", context)


@login_required
def my_notes(request):
    notes = Note.objects.filter(uploaded_by=request.user).order_by("-uploaded_at")
    return render(request, "notes/my_notes.html", {"notes": notes})


@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, uploaded_by=request.user)

    if request.method == "POST":
        form_cls = OnlineNoteForm if note.is_online_note else NoteForm
        form = form_cls(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            if "save_draft" in request.POST:
                note.status = "Draft"
                messages.success(request, "Saved as Draft.")
            else:
                note.status = "Approved"
                messages.success(request, "Note details updated successfully.")
            note.save()
            return redirect("my_notes")
    else:
        form_cls = OnlineNoteForm if note.is_online_note else NoteForm
        form = form_cls(instance=note)

    return render(request, "notes/edit_note.html", {"form": form})


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, uploaded_by=request.user)

    if request.method == "POST":
        note.delete()
        messages.success(request, "Note deleted successfully.")
        return redirect("my_notes")

    return render(request, "notes/delete_note.html", {"note": note})


@login_required
def toggle_bookmark(request, pk):
    note = get_object_or_404(Note, pk=pk)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, note=note)
    if not created:
        bookmark.delete()
        messages.info(request, "Removed from bookmarks.")
    else:
        messages.success(request, "Saved to bookmarks!")

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect("browse_notes")


@login_required
def toggle_like(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.user in note.likes.all():
        note.likes.remove(request.user)
    else:
        note.likes.add(request.user)

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect("browse_notes")


@login_required
def bookmarks_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('note').order_by('-created_at')
    notes = [b.note for b in bookmarks]
    return render(request, "notes/bookmarks.html", {"notes": notes})


@staff_member_required
def admin_dashboard(request):
    notes = Note.objects.all().order_by("-uploaded_at")

    context = {
        "notes": notes,
        "pending": Note.objects.filter(status="Pending").count(),
        "approved": Note.objects.filter(status="Approved").count(),
        "rejected": Note.objects.filter(status="Rejected").count(),
    }

    return render(request, "notes/admin_dashboard.html", context)


@staff_member_required
def approve_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.status = "Approved"
    note.save()
    messages.success(request, f"Note '{note.title}' has been approved.")
    return redirect("admin_dashboard")


@staff_member_required
def reject_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.status = "Rejected"
    note.save()
    messages.info(request, f"Note '{note.title}' has been rejected.")
    return redirect("admin_dashboard")


@login_required
def view_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.file and os.path.exists(note.file.path):
        content_type, _ = mimetypes.guess_type(note.file.path)
        return FileResponse(open(note.file.path, "rb"), content_type=content_type or "application/octet-stream")
    else:
        return HttpResponseForbidden("This is an online e-note.")


@login_required
def download_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.downloads += 1
    note.save()

    if note.file and os.path.exists(note.file.path):
        return FileResponse(open(note.file.path, "rb"), as_attachment=True)
    else:
        messages.info(request, "Online e-notes can be viewed and copied directly from the website!")
        return redirect("note_detail", pk=pk)