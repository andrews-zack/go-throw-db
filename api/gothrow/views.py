from django.shortcuts import render
from django.http.response import Http404
from rest_framework import status, viewsets, generics, authentication, permissions
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
# from rest_framework import filters


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get']
    permission_classes = (permissions.AllowAny,)
    # def get_queryset(self):
    #     queryset = Course.objects.all()

class HoleViewSet(ModelViewSet):
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer
    http_method_names = ['get']
    permission_classes = (permissions.AllowAny,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get"]
    permission_classes = (permissions.AllowAny,)

class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)

class RoundsViewSet(ModelViewSet):
    queryset= Rounds.objects.all()
    serializer_class = RoundsSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (permissions.AllowAny,)

class ScoresViewSet(ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoresSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (permissions.AllowAny,)
