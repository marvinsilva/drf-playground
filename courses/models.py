from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255, verbose_name="Course Title")
    url = models.URLField(unique=True, verbose_name="Course URL")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title


class Evaluation(Base):
    course = models.ForeignKey(
        Course, related_name="Evaluations", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, verbose_name="Evaluator Name")
    email = models.EmailField()
    comment = models.TextField(blank=True, default="", verbose_name="Comment")
    evaluation = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Evaluation Score"
    )

    class Meta:
        verbose_name = "Evaluation"
        verbose_name_plural = "Evaluations"
        unique_together = ["email", "course"]

    def __str__(self):
        return (
            f"{self.name} rated the course {self.course} with grade {self.evaluation}"
        )
