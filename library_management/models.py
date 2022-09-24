from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
# Create your models here.
GENDER_CHOICE = (
    ('Male','Male'),
    ('Female', 'Female')
)
USER_TYPE = (
    ('COLLAGE','COLLAGE'),
    ('BOOK','BOOK'),
    ('LIBRARIAN','LIBRARIAN')
)
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/' , blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICE, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE,default='COLLAGE',max_length=10)
    address = models.TextField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_created = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
      return "{}".format(self.email)