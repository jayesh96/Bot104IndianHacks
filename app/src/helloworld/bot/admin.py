from django.contrib import admin

# Register your models here.

from .models import Hospital,HospitalBeds,HospitalRating

admin.site.register(Hospital)
admin.site.register(HospitalBeds)
admin.site.register(HospitalRating)