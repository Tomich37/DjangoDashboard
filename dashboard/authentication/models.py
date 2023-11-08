from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None):
        if not login:
            raise ValueError('The Login field must be set')
        
        if not password:
            raise ValueError('The Password field must be set')

        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        user = self.create_user(login, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UsersModel(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['password']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users',  # Добавьте эту строку для указания связанного имени
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получает все разрешения, предоставленные каждой из своих групп.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users',  # Добавьте эту строку для указания связанного имени
        blank=True,
        help_text='Конкретные разрешения для этого пользователя.'
    )

    def __str__(self):
        return self.login
    
    class Meta:
        app_label = 'authentication'
        db_table = 'users'
