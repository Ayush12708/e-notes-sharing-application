from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home app
    path('', include('home.urls')),

    # Accounts app
    path('accounts/', include('accounts.urls')),

    # Dashboard app
    path("dashboard/", include("dashboard.urls")),

    # Notes app
    path("notes/", include("notes.urls")),

    # Media files serving for production deployment
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]