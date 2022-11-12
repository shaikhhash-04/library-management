from django.db import models
from traitlets import default
from app.manager import CustomManager
# Create your models here.
Type_Choice =(
('Non-Fiction','Non-Fiction'),('Edited','Edited'),('Reference','Reference'),('Fiction','Fiction'))

class Task(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    type=models.CharField(choices=Type_Choice, max_length=100)
    is_deleted=models.CharField(max_length=2,default='n')
    

# Create your models here.
