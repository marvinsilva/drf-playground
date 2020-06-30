from django.contrib import admin
from school.courses.models import Course, Evaluation


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "created_at", "updated_at", "active")


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "name",
        "email",
        "evaluation",
        "created_at",
        "updated_at",
        "active",
    )
