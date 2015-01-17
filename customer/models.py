from django.db import models
from datetime import datetime
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
	product = models.CharField(max_length=100,)
	quantity= models.IntegerField(max_length=10)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	total = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.product

class Invoice(models.Model):
	customer=models.ForeignKey(User, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	total_amount= models.DecimalField(max_digits=10, decimal_places=2)
	total_quantity= models.DecimalField(max_digits=10, decimal_places=2)
	transaction= models.ManyToManyField(Transaction)

	def __unicode__(self):
		return self.customer.username
