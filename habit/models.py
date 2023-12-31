import datetime
from django.db import models

from config import settings
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    PERIOD_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
    ]
    habit_name = models.CharField(max_length=100, verbose_name='Habit Name')
    habit_description = models.TextField(verbose_name='Habit Description', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='habits', on_delete=models.CASCADE,
                              verbose_name='Habit Creator')

    habit_action = models.TextField(verbose_name='Habit Action')
    is_pleasant = models.BooleanField(verbose_name='Is Pleasant', default=False)
    pleasant_habit = models.ManyToManyField('self', symmetrical=False, verbose_name='Pleasant Habit', blank=True)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, verbose_name='Period In Minutes', default='DAILY')
    reward = models.TextField(verbose_name='Reward', **NULLABLE)
    time_to_complete = models.PositiveIntegerField()
    is_public = models.BooleanField(verbose_name='is Public', default=False)

    def __str__(self):
        return f"{self.owner}'s habit: {self.habit_action}"

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
