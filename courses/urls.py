from courses.views import CourseAPIView
from courses.views import EvaluationAPIView
from django.urls import path

urlpatterns = [
    path("courses/", CourseAPIView.as_view(), name="courses"),
    path("evaluations/", EvaluationAPIView.as_view(), name="evaluations"),
]
