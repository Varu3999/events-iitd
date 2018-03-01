from django.db import models

# Create your models here.

class event(models.Model):
    name = models.CharField(max_length=100,default="hi")
    date = models.DateField()
    time = models.TimeField()
    info = models.CharField(max_length=1000)
    venue = models.CharField(max_length=100)
    image = models.URLField()



class register(models.Model):
    event = models.ForeignKey(event,on_delete= models.CASCADE)
    email = models.EmailField(null= False)
    name = models.CharField(max_length=100, null= False)

    class Meta:
        unique_together = ('email', 'event')


class sa(models.Model):
    msg = models.CharField(max_length=10000)


