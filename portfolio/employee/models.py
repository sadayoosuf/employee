from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField()
    email=models.EmailField(max_length=200)
    image=models.ImageField(upload_to="images",blank=True,null=True)


    def __str__(self):
        return self.ename
