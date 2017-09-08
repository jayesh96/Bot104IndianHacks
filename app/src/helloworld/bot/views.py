from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .models import Hospital,HospitalBeds,HospitalRating,HospitalBooking

def HospitalList(request):
	h_list = []
	obj = Hospital.objects.filter(pincode=pincode)
	for i in obj:

		a = {}
		obj_bed = HospitalBeds.objects.get(title_id=i)
		
		a['avg_rating'] = i.avg_rating
		a['room_type_a'] = obj_bed.room_type_a
		a['room_type_b'] = obj_bed.room_type_b
		a['address'] = i.address
		a['pincode'] = i.pincode
		a['contact'] = i.contact
		a['hospital_name'] = i.title

		h_list.append(a)

	print (h_list)


	return JsonResponse(h_list,safe=False,json_dumps_params={'indent': 2})



def HospitalBookingNotify(request):
	context = {}
	print request.GET
	obj = HospitalBooking.objects.all()
	print(obj.count())

	return render(request,"hospital-dashboard.html",{"count":obj.count()})