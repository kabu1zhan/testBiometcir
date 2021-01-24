from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Person
        fields = ('iin', 'age')
