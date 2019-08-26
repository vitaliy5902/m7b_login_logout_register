from django.db import models

from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
