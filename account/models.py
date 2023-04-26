from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.


class User(AbstractUser):
    is_patient= models.BooleanField('Is patient', default=False)
    is_doctor= models.BooleanField('Is doctor', default=False)
    image=models.ImageField(upload_to="images/",blank=False,null=False)
    address=models.TextField(max_length=250)

