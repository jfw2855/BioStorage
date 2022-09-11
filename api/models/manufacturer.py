from django.db import models

# Create your models here.
class Manufacturer(models.Model):
  # define fields
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    
    return f"{self.name}"

  def as_dict(self):
    return {
        'id': self.id,
        'name': self.name
    }
