from courses.views import CourseAPIView
from courses.views import CoursesAPIView
from courses.views import CourseViewSet
from courses.views import EvaluationAPIView
from courses.views import EvaluationsAPIView
from courses.views import EvaluationViewSet
from django.urls import path
from rest_framework.routers import SimpleRouter

# api/v2
router = SimpleRouter()
router.register("courses", CourseViewSet)
router.register("evaluations", EvaluationViewSet)

# api/v1
urlpatterns = [
    path("courses/", CoursesAPIView.as_view(), name="courses"),
    path("courses/<int:pk>/", CourseAPIView.as_view(), name="course"),
    path(
        "courses/<int:course_pk>/evaluations/",
        EvaluationsAPIView.as_view(),
        name="course_evaluations",
    ),
    path(
        "courses/<int:course_pk>/evaluations/<int:evaluation_pk>/",
        EvaluationAPIView.as_view(),
        name="course_evaluation",
    ),
    path("evaluations/", EvaluationsAPIView.as_view(), name="evaluations"),
    path(
        "evaluations/<int:evaluation_pk>/",
        EvaluationAPIView.as_view(),
        name="evaluation",
    ),
]
