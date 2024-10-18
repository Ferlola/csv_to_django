from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('',views.index, name='index'),
    path('book', views.BookView.as_view(), name='book'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name="book_detail"),
    path('search/', views.search, name='search')
]
