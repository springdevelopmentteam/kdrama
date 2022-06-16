from .models import Actor
from rest_framework import serializers

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor 
        fields = ['id', 'actor_image', 'actor_name', 'surname', 'dob', 'zodic_sign', 'drama_name', 'actor_profile', 'update_datetime'] 
