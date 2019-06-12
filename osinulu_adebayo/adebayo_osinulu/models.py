from django.db import models

# Create your models here.
class Contact(models.Model):
    First_Name = models.CharField(max_length =100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_Number = models.DecimalField(max_digits=25, decimal_places=0)
    Message = models.TextField()

    def __str__(self):
        return f" Message from {self.First_Name} {self.Last_Name}"