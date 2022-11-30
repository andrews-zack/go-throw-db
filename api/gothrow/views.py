from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
# from rest_framework import filters


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get']


class HoleViewSet(ModelViewSet):
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer
    http_method_names = ['get']
