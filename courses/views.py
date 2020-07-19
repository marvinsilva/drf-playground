from courses.models import Course
from courses.models import Evaluation
from courses.serializers import CourseSerializer
from courses.serializers import EvaluationSerializer
from rest_framework import generics


class CoursesAPIView(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Course model instance.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Course model instance.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluationsAPIView(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a Evaluation model instance.
    """

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Evaluation model instance.
    """

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
