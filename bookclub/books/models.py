from django.db import models
from django.utils import timezone
import datetime

class Author(models.Model):
    #
    def __str__(self):
        return self.first_name + " " + self.last_name

    first_name = models.CharField('first name',max_length=50)
    last_name = models.CharField('last name',max_length=50)    
    prefix = models.CharField(max_length=4)
    suffix = models.CharField(max_length=4)

class Work(models.Model):
    # 
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=30)

    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
