from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from notes.models import Note, Bookmark

@login_required
def dashboard(request):
    # User's own notes summary
    my_notes = Note.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')
    total_notes = my_notes.count()
    approved_count = my_notes.filter(status="Approved").count()
    pending_count = my_notes.filter(status="Pending").count()
    total_downloads = my_notes.aggregate(Sum('downloads'))['downloads__sum'] or 0

    # Saved Bookmarks
    user_bookmarks = Bookmark.objects.filter(user=request.user).select_related('note').order_by('-created_at')[:5]
    total_bookmarks = Bookmark.objects.filter(user=request.user).count()

    # Study Materials Exploration Data
    popular_notes = Note.objects.filter(status="Approved").order_by("-downloads")[:6]
    recent_community_notes = Note.objects.filter(status="Approved").order_by("-uploaded_at")[:6]

    # Subject counts for study category exploration
    subjects_list = [
        {'code': 'DSA', 'name': 'Data Structures & Algo', 'icon': '⚡'},
        {'code': 'DBMS', 'name': 'Database Systems', 'icon': '🗄️'},
        {'code': 'OS', 'name': 'Operating Systems', 'icon': '💻'},
        {'code': 'CN', 'name': 'Computer Networks', 'icon': '🌐'},
        {'code': 'PYTHON', 'name': 'Python Programming', 'icon': '🐍'},
        {'code': 'JAVA', 'name': 'Java Development', 'icon': '☕'},
    ]

    for subj in subjects_list:
        subj['count'] = Note.objects.filter(status="Approved", subject=subj['code']).count()

    user_bookmarked_ids = Bookmark.objects.filter(user=request.user).values_list('note_id', flat=True)

    context = {
        "my_notes": my_notes[:5],
        "total_notes": total_notes,
        "approved_count": approved_count,
        "pending_count": pending_count,
        "total_downloads": total_downloads,
        "total_bookmarks": total_bookmarks,
        "user_bookmarks": user_bookmarks,
        "popular_notes": popular_notes,
        "recent_community_notes": recent_community_notes,
        "subjects_list": subjects_list,
        "user_bookmarked_ids": list(user_bookmarked_ids),
    }

    return render(request, "dashboard/dashboard.html", context)