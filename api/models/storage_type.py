from django.db import models

class StorageType(models.Model):
  
  type = models.CharField(max_length=30)
  storage_temp = models.CharField(max_length=30)

  def __str__(self):
    
    return f"{self.type}: temp: {self.storage_temp}"

  def as_dict(self):
    return {
        'id': self.id,
        'type': self.type,
        'storage_temp':self.storage_temp,
    }
