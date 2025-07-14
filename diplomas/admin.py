from django.contrib import admin
from .models import Diploma


@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ("diploma_number", "full_name", "issue_date", "created_at")
    search_fields = ("diploma_number", "full_name")
