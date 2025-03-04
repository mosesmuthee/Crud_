from django.urls import path

# from crud_moses.urls import urlpatterns
from .import views

urlpatterns = [
    path('', views.user_list, name='listingpage.html'),

    path('Add/', views.AddUser),

    path('Edit/<id>', views.EditUser),

    path('Delete/<id>', views.DeleteUser),

    path('View/<id>', views.ViewUser),
]