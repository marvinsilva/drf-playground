from courses.views import CourseAPIView
from courses.views import CoursesAPIView
from courses.views import EvaluationAPIView
from courses.views import EvaluationsAPIView
from django.urls import path

urlpatterns = [
    path("courses/", CoursesAPIView.as_view(), name="courses"),
    path("courses/<int:pk>/", CourseAPIView.as_view(), name="course"),
    path("evaluations/", EvaluationsAPIView.as_view(), name="evaluations"),
    path("evaluations/<int:pk>/", EvaluationAPIView.as_view(), name="evaluation"),
]
