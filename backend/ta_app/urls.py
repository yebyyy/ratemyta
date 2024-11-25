from django.urls import path, include
from rest_framework.routers import DefaultRouter 
# router is a way to automatically determine the URL conf for a set of views
# DefaultRouter is a simple router which creates a set of default routes for the views
from .views import SchoolViewSet, TAViewSet, ReviewViewSet, RegisterUserViewSet

router = DefaultRouter()
#.register() method is used to register a viewset with the router
router.register(r'schools', SchoolViewSet)  # /schools is registered with SchoolViewSet
router.register(r'tas', TAViewSet) # /tas is registered with TAViewSet
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)), # include all the urls from the router
    path('register/', RegisterUserViewSet.as_view(), name='register')
]