from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Project(models.Model):
    """Project model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField()


    def __str__(self):
        """Return project title and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'