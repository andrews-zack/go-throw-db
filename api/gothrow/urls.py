from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'holes', HoleViewSet)

urlpatterns = [
    path('', include(router.urls))
]