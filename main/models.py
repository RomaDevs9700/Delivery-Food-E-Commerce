from django.db import models
from django.utils import timezone
from uuid import uuid4


class Home(models.Model):
	title = models.CharField(max_length=128, blank=False, null=False)
	description = models.TextField(max_length=2048, blank=True, null=True)

	def __str__(self):
		return self.title

class About(models.Model):
	title = models.CharField(max_length=128, blank=False, null=False)
	description = models.TextField(max_length=2048, blank=True, null=True)
	image = models.ImageField(default=None, blank=True, null=True)

	def __str__(self):
		return self.title


class Menu(models.Model):
	def dp_rename_and_path(instance, filename):
		extension = filename.split('.')[-1]
		time_stamp = timezone.now()
		time_stamp = time_stamp.strftime("%d-%m-%Y_%I-%M-%S%p")
		path = 'menu_pics/{title}/{time_stamp}_{randomstring}.{extension}'.format(
			title = instance.title, 
			time_stamp = time_stamp, 
			randomstring = uuid4().hex, 
			extension = extension,
		)
		print(path)
		return path
		
	title = models.CharField(max_length=128, blank=False, null=False)
	price = models.CharField(max_length=64, blank=False, null=False)
	discount = models.CharField(max_length=64, blank=True, null=True)
	image = models.ImageField(default='menu_pics/default_menu.jpg', upload_to = dp_rename_and_path)
	
	def add_to_card(self, *args):
		pass

	def __str__(self):
		return self.title

class Products(models.Model):
	def dp_rename_and_path(instance, filename):
		extension = filename.split('.')[-1]
		time_stamp = timezone.now()
		time_stamp = time_stamp.strftime("%d-%m-%Y_%I-%M-%S%p")
		path = '{title}/{time_stamp}_{randomstring}.{extension}'.format(
			title = instance.title, 
			time_stamp = time_stamp, 
			randomstring = uuid4().hex, 
			extension = extension,
		)
		print(path)
		return path

	title = models.CharField(max_length=128, null=True, blank=True)
	price = models.CharField(max_length=64, blank=False, null=False)
	discount = models.CharField(max_length=64, blank=True, null=True)
	image = models.ImageField(default='products_pics/default_product.jpg', upload_to = dp_rename_and_path)

	def star(self, *args):
		pass
	
	def like(self, *args):
		pass

	def view(self, *args):
		pass

	def add_to_card(self, *args):
		pass

	def __str__(self):
		return self.title    


class Contact(models.Model):
	name = models.CharField(max_length=128, blank=False, null=False)
	email = models.EmailField(unique=True, blank=False, null=False)
	number = models.SmallIntegerField(unique=True)  
	review = models.TextField(max_length=2048, default=None) 
	check_display = models.BooleanField(default=False)

	def __str__(self):
		return self.name