from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.description

class Members(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + ' '+ self.lname

class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    school = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name +' '+self.school