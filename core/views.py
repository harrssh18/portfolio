from django.shortcuts import render

# Create your views here.
def home(requets):
	context = {'home':'active'}
	return render(requets,'core/home.html',context)

def contact(requets):
	context = {'contact':'active'}
	return render(requets,'core/contact.html',context)

