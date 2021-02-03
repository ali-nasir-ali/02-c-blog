from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# each class is going to be a tables in a database
class Post(models.Model): 
# now the atributes is going to be a differnt filed in the database
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
#here the post have one to many relationship with user through foreignkey
     auther = models.ForeignKey(User, on_delete=models.CASCADE)

