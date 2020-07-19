from courses.models import Course
from courses.models import Evaluation
from courses.serializers import CourseSerializer
from courses.serializers import EvaluationSerializer
from rest_framework import generics
from rest_framework.generics import get_object_or_404


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

    def get_queryset(self):
        if self.kwargs.get("course_pk"):
            return self.queryset.filter(course_id=self.kwargs.get("course_pk"))
        return self.queryset.all()


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a Evaluation model instance.
    """

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get("course_pk"):
            return get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get("course_pk"),
                pk=self.kwargs.get("evaluation_pk"),
            )
        return get_object_or_404(
            self.get_queryset(), pk=self.kwargs.get("evaluation_pk")
        )
