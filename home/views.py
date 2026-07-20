from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User
from notes.models import Note
from notes.views import ensure_default_seed_notes

def index(request):
    ensure_default_seed_notes()

    trending_notes = Note.objects.filter(status="Approved").order_by("-downloads", "-uploaded_at")[:6]
    total_notes_count = Note.objects.filter(status="Approved").count()
    total_downloads_count = Note.objects.aggregate(Sum('downloads'))['downloads__sum'] or 0
    total_students_count = User.objects.count()

    context = {
        "trending_notes": trending_notes,
        "total_notes_count": total_notes_count,
        "total_downloads_count": total_downloads_count,
        "total_students_count": total_students_count,
    }
    return render(request, "home/index.html", context)