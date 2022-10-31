from django.urls import path
from . import views


app_name = 'manager'
urlpatterns = [
    path('photos', views.photo_list),
    path('photos/<pk>', views.photo_detail),
]
