from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from actor import views

router = routers.DefaultRouter()
router.register(r'actors', views.ActorViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]