from django.db import models
from django.contrib.auth.models import User

class Stream(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(max_length=200, upload_to='img')
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Group(models.Model):
    title = models.CharField(max_length=10)
    stream = models.ManyToManyField(Stream)
    price = models.IntegerField()

    def stream_list(self):
        list_stream = []
        for i in self.stream.all():
            list_stream.append(i)
        return list_stream

    def __str__(self):
        return self.title

class Membership(models.Model):
    start_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


    def __str__(self):
        return "%s - %s" % (self.user, self.group)


















