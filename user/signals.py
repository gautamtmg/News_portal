from django.dispatch import receiver
from django.db.models.signals import (post_save,)
from django.contrib.auth.models import User


from .models import UserProfile

@receiver(post_save, sender=User)
def update_user_profiel(sender, instance, created, **kwargs):
    # Update user profile
    if created:
        UserProfile.objects.create(
            user = instance
        )