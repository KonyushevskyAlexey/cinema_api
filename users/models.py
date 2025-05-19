from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('cashier', 'Cashier'),
        ('visitor', 'Visitor'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='visitor')
    phone = models.CharField(max_length=20, blank=True)
    
    # Добавляем related_name для разрешения конфликтов
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='cinema_user_set',  # Уникальное имя
        related_query_name='cinema_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='cinema_user_set',  # Уникальное имя
        related_query_name='cinema_user',
    )
    
    def is_admin(self):
        return self.role == 'admin'
    
    def is_cashier(self):
        return self.role == 'cashier'
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
