from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:75]

    def pub_date(self):
        return self.publish_date.strftime("%b %e %Y")

