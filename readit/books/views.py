from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def list_books(request):
	#books=
	# Get logged in username
	#return HttpResponse(request.user.username)
	'''
	Lis books that have reviews

	'''
	books = Book.objects.exclude(date_reviewed__isnull=True
												).prefetch_related('authors')
	context = {'books': books }
	return render(request,'list.html',context)