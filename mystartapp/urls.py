from django.urls import path

# from crud_moses.urls import urlpatterns
from .import views

urlpatterns = [
    path('', views.user_list, name='listingpage.html'),

    path('Add/', views.AddUser),

]