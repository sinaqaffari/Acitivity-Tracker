from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    
    CATEGORY_CHOICES = [
        ('code', 'Coding'),
        ('read', 'Reading'),
        ('debug', 'Debugging'),
        ('meet', 'Metting'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.duration_minutes}min"
    



    