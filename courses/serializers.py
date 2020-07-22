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

    # Nested Relationship
    # evaluations = EvaluationSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    # evaluations = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="evaluation-detail")

    # Primary Key Related Field
    evaluations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "url",
            "created_at",
            "active",
            "evaluations",
        )
