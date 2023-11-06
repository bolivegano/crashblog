
from . import views
from django.urls import path


urlpatterns = [
    
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name="post_detail"),
    path('<slug:slug>/', views.category, name="category_detail"),
] 
