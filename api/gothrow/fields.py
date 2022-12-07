from rest_framework import serializers
from .models import *


class CourseListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.course_name

    def to_internal_value(self, data):
        return Course.objects.get(course_name=data)


class HoleListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.hole_num

    def to_internal_value(self, data):
        return Hole.objects.get(hole_num=data)


class UserListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.username

    def to_internal_value(self, data):
        return CustomUser.objects.get(username=data)