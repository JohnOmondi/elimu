

from django.contrib import admin
from django.urls import path
from elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('info/', views.information, name='info'),
    path('tables/', views.table, name='tables'),
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
