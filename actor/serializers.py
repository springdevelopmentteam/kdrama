from .models import Actor
from rest_framework import serializers

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor 
        fields = ['id', 'actor_image', 'actor_name', 'dob', 'zodic_sign', 'drama_name', 'actor-profile', 'update_datetime'] 