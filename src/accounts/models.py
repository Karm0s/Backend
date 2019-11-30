from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        """
        Creates and saves a new user.
        """
        if not email:
            raise ValueError('User must have a valid email address.')
        
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email=None, password=None):
        """
        Creates and saves a new staff user.
        """
        if not email:
            raise ValueError('User must have a valid email address.')
        
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.staff = True

        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        """
        Creates and saves a new superuser.
        """
        if not email:
            raise ValueError('User must have a valid email address.')
        
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.staff = True
        user.admin = True

        user.save(using=self._db)
        return user
    



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    user_name = models.CharField(verbose_name='username', max_length=50, unique=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email
    
    def get_username(self):
        return super().get_username()
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

