from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
router.register(f'albums', views.AlbumsViewSet)

app_name = 'manager'
urlpatterns = [
    path('', include(router.urls)),
]
