from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, username,  e_mail, password=None):
        if not username:
            raise ValueError('The username must be set')

        user = self.model(
            username=username,
            e_mail=e_mail,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, e_mail):
        user = self.create_user(
            username=username,
            password=password,
            e_mail=e_mail,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_column='user_id', primary_key=True, max_length=200, unique=True)
    password = models.CharField(db_column='PW', max_length=200)  # Field name made lowercase.
    last_login = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_superuser = models.IntegerField(blank=True, null=True, default=False)
    e_mail = models.CharField(max_length=320, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True, default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['e_mail']

    class Meta:
        db_table = 'user'

    @property
    def is_staff(self):
        return self.is_superuser
