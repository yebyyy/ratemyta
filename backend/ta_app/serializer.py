from rest_framework import serializers
from .models import User, School, TA, Review

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__' # fields = ['id', 'name']

class TASerializer(serializers.ModelSerializer):
    class Meta:
        model = TA
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'