from courses.models import Course
from courses.models import Evaluation
from courses.serializers import CourseSerializer
from courses.serializers import EvaluationSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


"""
API version 1 api/v1 using generic views
"""


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


"""
API version 2 api/v2 using viewsets
"""


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def evaluations(self, request, pk=None):
        self.pagination_class.page_size = 2
        evaluations = Evaluation.objects.filter(course_id=pk)
        page = self.paginate_queryset(evaluations)

        if page is not None:
            serializer = EvaluationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
