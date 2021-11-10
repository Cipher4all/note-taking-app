from django.db import models

# Create your models here.
class MyNote(models.Model):
    heading = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="media")
    describe = models.TextField(default= 'Add a new note')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headings