from django.db import models
from .storage_type import StorageType

class Storage(models.Model):
  
  is_full = models.BooleanField(default=False)
  location = models.CharField(max_length=50)
  storage_type = models.ForeignKey(
    'StorageType',
    on_delete=models.CASCADE,
    related_name='storage_type_id'
  )

  def __str__(self):
    
    return f"Storage Full: {self.is_full}, Location: {self.location} Storage Type: {self.storage_type}"

  def as_dict(self):
    return {
        'id': self.id,
        'is_full':self.is_full,
        'location': self.location,
        'storage_type':self.storage_type,
    }
