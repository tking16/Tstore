from django.db import models

# Create your models here.
class Shirt(models.Model):
	name = models.CharField(max_length=200)
	stock = models.IntegerField(default=70)
	image = models.CharField(max_length=1000)
	price = models.IntegerField(default=7)
	
	def __str__(self):
		return self.name + ": " + str(self.stock)
	
	def out_of_stock(self):
		if self.stock == 0:
			return self.name