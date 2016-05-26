from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    class Meta:
        model = Resume

admin.site.register(Resume, ResumeAdmin)
