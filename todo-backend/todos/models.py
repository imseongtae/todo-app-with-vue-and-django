from django.db import models

# Create your models here.
class Todo(models.Model):
  todo = models.CharField(max_length=512)
  create_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.todo

