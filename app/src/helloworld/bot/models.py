from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Hospital(models.Model):
	title = models.CharField(max_length=200,null=False, blank=False)
	address = models.CharField(max_length=200,null=False, blank=False) 
	pincode = models.IntegerField(null=False, blank=False)
	contact = models.CharFieldField(null=False, blank=False)
	avg_rating = models.DecimalField(max_digits=2,decimal_places=2,null=False, blank=False,default=0.00)


	class Meta:
		ordering = ["-avg_rating"]
		verbose_name = 'Hospital'
		verbose_name_plural = "Hospitals"

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)



class HospitalBeds(models.Model):
	title = models.ForeignKey(Hospital,on_delete=models.CASCADE)
	is_bed_available = models.BooleanField(default=True)
	room_type_a = models.IntegerField(null=False,blank=False)
	room_type_b = models.IntegerField()


	class Meta:
		ordering = ["is_bed_available"]
		verbose_name = 'Hospital Bed'
		verbose_name_plural = "Hospital Beds"

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)


class HospitalRating(models.Model):
	title = models.ForeignKey(Hospital,on_delete=models.CASCADE)
	google_rating = models.DecimalField(max_digits=2,decimal_places=2)
	user_rating = models.IntegerField()


	class Meta:
		verbose_name = 'Hospital Rating'
		verbose_name_plural = 'Hospital Ratings'

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)
