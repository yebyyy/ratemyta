from rest_framework import viewsets, generics, permissions
# viewsets is a collection of views (functions) that help us to create CRUD views
from .models import School, TA, Review, User
from .serializer import SchoolSerializer, TASerializer, ReviewSerializer, UserRegistrationSerializer


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def perform_destroy(self, serializer):
        if serializer.student == self.request.user:
            serializer.delete()
    def perform_update(self, serializer):
        if serializer.student == self.request.user:
            serializer.save()
            
class RegisterUserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
