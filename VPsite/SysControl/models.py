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


