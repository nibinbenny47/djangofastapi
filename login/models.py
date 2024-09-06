
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone, date_of_birth, address, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone, date_of_birth=date_of_birth, address=address,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, date_of_birth, address,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, phone, date_of_birth, address,  password, **extra_fields)
 
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    groups = models.ForeignKey(Group,on_delete=models.CASCADE, blank =True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'date_of_birth', 'address']

    def __str__(self):
        return self.email