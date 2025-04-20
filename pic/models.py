from django.db import models
from users.models import User


class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='images')
    content = models.ImageField(upload_to='contents/')
    description = models.CharField(max_length=250,null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pic: {self.id} by: @{self.user.username}'