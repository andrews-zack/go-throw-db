from rest_framework import serializers
from .models import *
from .fields import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password",]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance


class RoundsSerializer(serializers.ModelSerializer):
    course = CourseListingField(queryset=Course.objects.all())
    
    class Meta:
        model = Rounds
        # fields = ["id", "user", "course", "total_score"]
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    hole_list = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "course_name", "holes", "course_lat", "course_long", "hole_list",]

    def get_hole_list(self, obj):
        course = obj.id
        hole_list = Hole.objects.filter(course=course).order_by("hole_num")
        course_holes = []
        for item in hole_list:
            course_holes.append({
                "id": item.id,
                "hole_num": item.hole_num,
                "par": item.par,
                "length": item.length,
                "hole_lat": item.hole_lat,
                "hole_long": item.hole_long
            })
        return course_holes


class HoleSerializer(serializers.ModelSerializer):
    course = CourseListingField(queryset=Course.objects.all(), required=False)
    
    class Meta:
        model = Hole
        fields = ["id", "course", "hole_num", "par", "length", "hole_lat", "hole_long",]


class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = ["id", "user", "rounds", "hole", "score"]
