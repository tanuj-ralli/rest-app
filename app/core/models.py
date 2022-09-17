"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,  # it contains methods for authentication but not fields.
    PermissionsMixin,  # it has permission methods to assign to various users.
    BaseUserManager,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **kwargs):
        """Create, save and return new user."""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return new super user."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # field that we wish to use for authentication.
