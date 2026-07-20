from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_note, name="upload_note"),
    path("create-online/", views.create_online_note, name="create_online_note"),
    path("browse/", views.browse_notes, name="browse_notes"),
    path("detail/<int:pk>/", views.note_detail, name="note_detail"),
    path("my-notes/", views.my_notes, name="my_notes"),
    path("edit/<int:pk>/", views.edit_note, name="edit_note"),
    path("delete/<int:pk>/", views.delete_note, name="delete_note"),
    path("bookmark/<int:pk>/", views.toggle_bookmark, name="toggle_bookmark"),
    path("like/<int:pk>/", views.toggle_like, name="toggle_like"),
    path("bookmarks/", views.bookmarks_list, name="bookmarks"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("approve/<int:pk>/", views.approve_note, name="approve_note"),
    path("reject/<int:pk>/", views.reject_note, name="reject_note"),
    path("view/<int:pk>/", views.view_note, name="view_note"),
    path("download/<int:pk>/", views.download_note, name="download_note"),
]