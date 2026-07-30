from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """Show Profile fields directly inside the User edit page in Django Admin."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile (StudyVerse)'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    """Extended User admin that shows Profile inline."""
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_college', 'get_semester')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    def get_college(self, obj):
        try:
            return obj.profile.college
        except Profile.DoesNotExist:
            return '—'
    get_college.short_description = 'College'

    def get_semester(self, obj):
        try:
            return obj.profile.semester
        except Profile.DoesNotExist:
            return '—'
    get_semester.short_description = 'Semester'


# Unregister the default User admin and register our extended version
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
