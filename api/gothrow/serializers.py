from rest_framework import serializers
from .models import *
# from .fields import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username",]


class RoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rounds
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"