from courses.models import Course
from courses.models import Evaluation
from courses.serializers import CourseSerializer
from courses.serializers import EvaluationSerializer
from rest_framework import status
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

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EvaluationAPIView(APIView):
    """
    Evaluation APIView
    """

    def get(self, request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
