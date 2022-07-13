from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

#for User 
from django.contrib.auth.models import User

class Entry(models.Model):
   user = models.ForeignKey(User, verbose_name=u"пользователь", blank=True, null=True, on_delete=models.CASCADE)
   title = models.CharField(u"заголовок", max_length=100)

   def __unicode__(self):
      return self.title

   class Meta:
      verbose_name = u"""запись"""
      verbose_name_plural = u"""записи"""


#__________________________________________________________________________________________

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)
    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    class Meta:
        unique_together = ("name", "year", )

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)