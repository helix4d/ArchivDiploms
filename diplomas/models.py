from django.db import models
from django.contrib.auth import get_user_model


def diploma_upload_path(instance, filename):
    return f"diplomas/{filename}"


class Diploma(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    issue_date = models.DateField(verbose_name="Issue Date")
    diploma_number = models.CharField(max_length=100, unique=True, verbose_name="Diploma Number")
    diploma_file = models.FileField(upload_to=diploma_upload_path, verbose_name="Diploma File")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.diploma_number}"
