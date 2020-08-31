from django.urls import path, include
from . import views
from django.views import View
from . views import Home, Viewproducts, Delete, Edit, Update

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('viewproducts/', Viewproducts.as_view(), name='viewproducts'),
    path('edit/<int:id>', Edit.as_view(), name='edit'),
    path('update/<int:id>', Update.as_view(), name='update'),
    path('delete/<int:id>', Delete.as_view(), name='delete'),
    #  path for our rest api
    path('api/', include('MyApp.api.urls'))   
]
