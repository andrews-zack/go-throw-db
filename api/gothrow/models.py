from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Rounds(models.Model):
    total_score = models.IntegerField(null=False, blank=True)
    course = models.ForeignKey("Course", on_delete=models.PROTECT)

class Course(models.Model):
    course_name = models.CharField(max_length=50, null=False, blank=True, unique=True)
    holes = models.IntegerField(null=False, blank=False)
    course_lat = models.DecimalField(max_digits=7, decimal_places=5, null=False, blank=True)
    course_long = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=True)

class Hole(models.Model):
    course = models.ForeignKey("Course", on_delete=models.PROTECT)
    hole_num = models.IntegerField(null=False, blank=True)
    par = models.IntegerField(null=False, blank=True)
    length = models.IntegerField(null=False, blank=True)
    hole_lat = models.DecimalField(max_digits=7, decimal_places=5, null=False, blank=True)
    hole_long = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=True)

class Scores(models.Model):
    score = models.IntegerField(null=False, blank=True)

class RoundScore(models.Model):
    rounds = models.ForeignKey("Rounds", on_delete=models.PROTECT)
    score = models.ForeignKey("Scores", on_delete=models.PROTECT)

class HoleScores(models.Model):
    hole = models.ForeignKey("Hole", on_delete=models.PROTECT)
    scores = models.ForeignKey("Scores", on_delete=models.PROTECT)

class UserScores(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.PROTECT)
    scores = models.ForeignKey("Scores", on_delete=models.PROTECT)
    
