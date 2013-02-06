import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Publie recemment?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice
		
class Party (models.Model):
	user1 = models.CharField(max_length=200)
	points1 = models.IntegerField()
	user2 = models.CharField(max_length=200)
	points2 = models.IntegerField()
	user3 = models.CharField(max_length=200)
	points3 = models.IntegerField()
	user4 = models.CharField(max_length=200)
	points4 = models.IntegerField()
	checked = models.IntegerField()
# Create your models here.
