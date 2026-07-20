from django.shortcuts import render
from notes.models import Note
from notes.views import ensure_default_seed_notes

def index(request):
    ensure_default_seed_notes()

    trending_notes = Note.objects.filter(status="Approved").order_by("-downloads")[:6]
    total_notes_count = Note.objects.filter(status="Approved").count()

    context = {
        "trending_notes": trending_notes,
        "total_notes_count": total_notes_count,
    }
    return render(request, "home/index.html", context)