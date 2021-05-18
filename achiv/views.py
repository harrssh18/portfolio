from django.shortcuts import render

# Create your views here.

def achiv(request):
	context = {'achiv':'active'}
	return render(request,'achiv/achiv.html',context)