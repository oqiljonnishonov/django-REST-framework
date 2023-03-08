from django.forms import ValidationError
from rest_framework import serializers
from .models import Actor , Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=('id','first_name','last_name','gender')
        
        def validate_birthdate(self,data):
            if data<data.fromisoformat('1950-10-01'):
                raise ValidationError(detail="Incorrect Data")
            return data


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('id','name','genre','year','actor')