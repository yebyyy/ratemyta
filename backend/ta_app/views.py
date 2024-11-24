from rest_framework import viewsets
# viewsets is a collection of views (functions) that help us to create CRUD views
from .models import School, TA, Review, User
from .serializer import SchoolSerializer, TASerializer, ReviewSerializer, UserSerializer


# class based views
# queryset defines what objects to get from the database
# serializer_class defines what serializer to use to serialize the objects
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class TAViewSet(viewsets.ModelViewSet):
    queryset = TA.objects.all()
    serializer_class = TASerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer