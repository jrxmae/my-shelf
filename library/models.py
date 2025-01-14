from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "To Be Read"), (1, "In Progress"), (2, "Read"), (3, "Did Not Finish"), (4, "Re-reading"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)