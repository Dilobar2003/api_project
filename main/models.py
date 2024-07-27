from django.db import models
from django.conf import settings

class PostModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
