from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ActorSerializer
from .models import Actor
# Create your views here.
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer