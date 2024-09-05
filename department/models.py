from django.db import models

# Create your models here.
class department(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    school = models.CharField(null=True,blank=True,max_length=100)

    def __str__(self):
        return self.name