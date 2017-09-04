from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .models import Hospital

def HospitalList(request):
	h_list = []
	obj = Hospital.objects.all()
	for i in obj:
		a = {}
		a['hospital_name'] = i.title
		a['address'] = i.address
		a['pincode'] = i.pincode
		a['contact'] = i.contact
		a['avg_rating'] = i.avg_rating
		h_list.append(a)

	print h_list


	return JsonResponse(h_list,safe=False,json_dumps_params={'indent': 2})