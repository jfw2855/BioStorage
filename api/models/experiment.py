from django.db import models
from django.contrib.auth import get_user_model

class Experiment(models.Model):
  # define fields
  name = models.CharField(max_length=100)
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Exp: {self.name}"

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'start_date': self.start_date,
        'end_date': self.end_date,
    }
