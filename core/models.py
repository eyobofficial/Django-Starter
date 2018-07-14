from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    """
    A base abstract model from which all other models will inherit.
    """
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True,
        help_text='Record first created date and time.'
    )
    modified = models.DateTimeField(
        auto_now=True,
        blank=True, null=True,
        help_text='Record last modified date and time.'
    )

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    """
    A custom user model for the built in Auth system
    """
    pass
