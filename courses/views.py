from courses.models import Course
from courses.models import Evaluation
from courses.serializers import CourseSerializer
from courses.serializers import EvaluationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class CourseAPIView(APIView):
    """
    Course APIView
    """

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class EvaluationAPIView(APIView):
    """
    Evaluation APIView
    """

    def get(self, request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)
