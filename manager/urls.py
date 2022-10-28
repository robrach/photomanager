from django.urls import path, include
from . import views
from rest_framework import routers
# from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)

app_name = 'manager'
urlpatterns = [
    path('', include(router.urls)),
    path('zdjecia', views.photo_list),
    path('zdjecia/<pk>', views.photo_detail),
]
