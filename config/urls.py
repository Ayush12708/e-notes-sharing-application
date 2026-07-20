from django.contrib import admin
from django.urls import path, include

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

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)