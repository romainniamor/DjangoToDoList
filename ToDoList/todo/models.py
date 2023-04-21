from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = True
        db_table = 'Category'


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=False)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(auto_now=True)
    priority = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Task'
        managed = True
        ordering = ['complete', '-priority', 'date']




