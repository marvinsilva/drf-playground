from courses.models import Course
from courses.models import Evaluation
from rest_framework import serializers


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"email": {"write_only": True}}
        model = Evaluation
        fields = (
            "id",
            "course",
            "name",
            "email",
            "comment",
            "evaluation",
            "created_at",
            "active",
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "url",
            "created_at",
            "active",
        )
