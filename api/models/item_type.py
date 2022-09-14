from django.db import models

class ItemType(models.Model):
  
  type = models.CharField(max_length=50, unique=True)
  description = models.TextField()

  def __str__(self):
    
    return f"Item Type: {self.type}"

  def as_dict(self):
    return {
        'id': self.id,
        'type': self.type,
    }
