#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class piece(models.Model):
	word = models.CharField(max_length=30)
	def __unicode__(self):
		return self.word

class entry(models.Model):
	username = models.ForeignKey(User)
	word = models.ForeignKey(piece)
	content = models.CharField(max_length=2000)
	rateCount = models.IntegerField(default="0")
	pub_date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.content