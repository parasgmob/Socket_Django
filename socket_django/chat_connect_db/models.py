from django.db import models

# Create your models here.
class ChatModel(models.Model):
  content   = models.CharField(max_length=1000)
  cratetime = models.DateTimeField(auto_now=True)
  group     = models.ForeignKey('Group',on_delete=models.CASCADE)

class Group(models.Model):
  name      = models.CharField(max_length=255)

  def __str__(self):
    return self.name
