from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View, DetailView
from django.http import HttpResponse
from .models import Book, Author

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

class AuthorList(View):
	def get(self, request):
# we could use Author.objects.all() if we wanted to retrieve all authors
		authors = Author.objects.annotate(
			 			published_books=Count('books')
			 			).filter(
			 			    published_books__lt=1
			 			)
			 			
		print (authors)
		context = { 'authors': authors }

		return render (request,'authors.html', context)

class BookDetail(DetailView):
	model = Book
	template_name = 'book.html'

class AuthorDetail(DetailView):
	model = Author
	template_name = 'author.html'