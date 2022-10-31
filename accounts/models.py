from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **additional_fields):
        """
        User  vith email registration
        """
        # Validation
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        unique=True
    )
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # date_joined = models.DateTimeField(default=timezone.now)
    # profile_photo = models.ImageField('Аватар', null=True, blank=True, upload_to='profile_images/')
    address = models.CharField(max_length=200, null=True, default='')
    # objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.email}'

    def get_full_name(self) -> str:
        # if self.first_name and self.last_name:
        #     return f'{self.first_name} {self.last_name}'
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    """
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    """
