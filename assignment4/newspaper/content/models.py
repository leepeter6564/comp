from django.db import models
from tinymce import models as tinymce_models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = tinymce_models.HTMLField()
    
    def __str__(self):
        return self.title

class Image(Content):
    # setting up relative path in django looked terrible, so I just used
    # absolute url pathing for images :/
    path = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)


    def __str__(self):
        return self.first_name + " " + self.last_name
    def die(self):
    	self.delete()
