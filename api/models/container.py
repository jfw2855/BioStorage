from django.db import models

class Container(models.Model):
  name = models.CharField(max_length=40)
  is_full = models.BooleanField(default=False)
  total_space = models.IntegerField()
  space_available = models.IntegerField()
  storage_location = models.CharField(max_length=50)
  storage_id = models.ForeignKey(
    'Storage',
    on_delete=models.CASCADE,
    related_name='storage_id'
  )

  def as_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'total_space': self.total_space,
        'space_available': self.space_available,
        'is_full':self.is_full,
        'storage_location': self.storage_location,
        'storage_id':self.storage_id,
    }
