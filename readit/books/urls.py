from django.conf.urls import url
from .views import AuthorList, list_books, BookDetail, AuthorDetail

urlpatterns=[

url('^$', list_books, name='books'),
url(r'^authors/$',AuthorList.as_view(), name='authors'),
url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
url(r'^authors/(?P<pk>[-\w]+)/$',AuthorDetail.as_view(), name='author-detail'),
]