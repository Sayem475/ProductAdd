from django.urls import path, include
from rest_framework import routers
from MyApp.api import views
router = routers.DefaultRouter()
router.register(r'ProductInfoDetail', views.ProductInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# the route of our api is 
# http://127.0.0.1:8000/api/

# THANK YOU SO MUCH