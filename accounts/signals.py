from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create a Profile every time a new User is created,
    regardless of HOW the user was created:
      - Website registration form
      - Django admin panel
      - Django shell / manage.py createsuperuser
      - MySQL Workbench (after next Django request triggers post_save)
      - Any API or backend script
    """
    if created:
        Profile.objects.get_or_create(
            user=instance,
            defaults={
                'phone': '',
                'college': 'Not specified',
                'semester': 1,
            }
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Ensure the Profile is saved whenever the User is saved.
    Also handles the case where an existing User somehow lost their Profile.
    """
    Profile.objects.get_or_create(
        user=instance,
        defaults={
            'phone': '',
            'college': 'Not specified',
            'semester': 1,
        }
    )
