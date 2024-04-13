from rest_framework import serializers


class UserRequestSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    age = serializers.IntegerField(min_value=0)
    gender = serializers.ChoiceField(choices=['Male', 'Female'])
    city = serializers.CharField(max_length=100)