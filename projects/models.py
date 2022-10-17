from django.db import models
from django.urls import reverse
from django.utils import timezone



class Project(models.Model):
    
    options = (
    ('active', 'Active'),
    ('completed', 'Completed'),
    )

    title = models.CharField(max_length = 250)
    publish_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='project_post')
    content= models.TextField()
    status = models.CharField(max_length = 10, choices = options, default='active')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])