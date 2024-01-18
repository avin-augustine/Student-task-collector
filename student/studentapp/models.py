from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from PIL import Image

# Create your models here.
class Course(models.Model):
    course=models.CharField(max_length=45) 
    
    def __str__(self):
        return self.course
    
class Days(models.Model):
    day=models.CharField(max_length=25)
    def __str__(self):
        return self.day

class Task(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Days=models.ForeignKey(Days,on_delete=models.CASCADE)
    task=models.CharField(max_length=45)
    
    def __str__(self):
        return self.task
 

class Student(models.Model):
    Name=models.CharField(max_length=25)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Days=models.ForeignKey(Days,on_delete=models.CASCADE)
    Task=ChainedForeignKey(Task,
         chained_field="Days",
         chained_model_field="Days",
         show_all=False,
         auto_choose=True,
         sort=True)
    Image=models.ImageField(upload_to='images')

    def logo_image(self):
        return('<img src="{0}" style="width: 145px; height:45px;" />'.format(self.Logo.url))


    logo_image.allow_tags=True

    
    def __str__(self):
        return self.Name