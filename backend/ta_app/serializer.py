from rest_framework import serializers
from .models import User, School, TA, Review

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__' # fields = ['id', 'name']

class TASerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = TA
        fields = '__all__'

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(ta=obj)
        if len(reviews) == 0:
            return 0
        total = 0
        for review in reviews:
            total += review.rating
        return total / len(reviews)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'ta', 'student', 'rating', 'review']
        read_only_fields = ['user']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user