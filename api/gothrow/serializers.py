from rest_framework import serializers
from .models import *
from .fields import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username",]


class RoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rounds
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    # hole_list = serializers.SerializerMethodField()
    hole_list = HoleListingField(many=True, queryset=Hole.objects.all(), required=False)

    class Meta:
        model = Course
        fields = "__all__"

    # def get_hole_list(self, obj):
    #     course = obj.id
    #     hole_list = CourseHole.objects.filter(course=course)
    #     course_holes = []
    #     for item in hole_list:
    #         course_holes.append(f"{item.hole}")
    #     return course_holes


class HoleSerializer(serializers.ModelSerializer):
    course = CourseListingField(queryset=Course.objects.all(), required=False)
    
    class Meta:
        model = Hole
        fields = ["id", "course", "hole_num", "par", "length", "hole_lat", "hole_long",]


class CourseHoleSerializer(serializers.ModelSerializer):
    hole = HoleListingField(queryset=Hole.objects.all(), required=False)

    class Meta:
        model = CourseHole
        fields = "__all__"