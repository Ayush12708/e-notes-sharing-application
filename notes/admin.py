from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "subject",
        "uploaded_by",
        "semester",
        "status",
        "uploaded_at",
    )

    list_filter = (
        "status",
        "subject",
        "semester",
    )

    search_fields = (
        "title",
        "uploaded_by__username",
    )