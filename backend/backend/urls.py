from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

#from sumari.views import sumarizacaoApi
from sumari.views import SumariViewSet

router = routers.DefaultRouter()
router.register(r'sumari', SumariViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  
]