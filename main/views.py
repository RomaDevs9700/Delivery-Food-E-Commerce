from django.shortcuts import render, redirect
from django.views import View

from .models import Home, About, Menu, Products, Contact
from .forms import ContactForm


class MainView(View): 
	def get(self, request):
		home = Home.objects.first()
		about = About.objects.first()
		menu = Menu.objects.all()
		products = Products.objects.all()
		contact  = Contact.objects.filter(check_display='True')
		return render(request, "index.html", {
			'home': home, 'about': about, 'menu': menu, 'products': products, 'contact': contact   
		})      
	
	def post(self, request):
		form = ContactForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data
			print(data)
			print(type(data))
			Contact.objects.create(
				name=data["name"],
				email=data["email"],
				number=data["number"],
				review=data["review"]
			) 
			return redirect('main')
		else:
			print("error: Invalid")

		return render(request, "index.html", {
			"form": form,
		})
	