from django.contrib import admin
from . models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	fieldsets= [
     ("Book Details",{'fields':['title','authors']}),
     ("Review",{'fields':['review','is_favourite','date_reviewed']}),
	]
     # Make the field uneditable
	#readonly_fields=  ('date_reviewed',)

	def book_authors(self,obj):
		return obj.list_authors()

	book_authors.short_description= 'Author(s)'
	list_editable = ('is_favourite',)
	list_display_links = ('title', 'date_reviewed',)
	list_filter = ('is_favourite','title',)
	search_fields = ('title','authors__name',)

	list_display = ('title','book_authors',
						'date_reviewed','is_favourite',)


# Register your models here.



admin.site.register(Author)