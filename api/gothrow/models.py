from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass


class Rounds(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.PROTECT)
    course = models.ForeignKey("Course", on_delete=models.PROTECT)
    total_score = models.IntegerField(null=False, default=0, blank=True)

class Course(models.Model):
    course_name = models.CharField(max_length=50, null=False, blank=True, unique=True)
    holes = models.IntegerField(null=False, blank=False)
    course_par = models.IntegerField(null=True, blank=True)
    course_lat = models.DecimalField(max_digits=7, decimal_places=5, null=False, blank=True)
    course_long = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=True)

    def __str__(self):
        return self.course_name

class Hole(models.Model):
    course = models.ForeignKey("Course", on_delete=models.PROTECT)
    hole_num = models.IntegerField(null=False, blank=True)
    par = models.IntegerField(null=False, blank=True)
    length = models.IntegerField(null=False, blank=True)
    hole_lat = models.DecimalField(max_digits=7, decimal_places=5, null=False, blank=True)
    hole_long = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=True)

class Scores(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.PROTECT)
    rounds = models.ForeignKey("Rounds", on_delete=models.PROTECT)
    hole = models.ForeignKey("Hole", on_delete=models.PROTECT)
    score = models.IntegerField(null=False, default=0, blank=True)


