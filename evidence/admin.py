from django.contrib import admin
from .models import Evidence

# Register your models here.
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'content', 'crime' ]

admin.site.register(Evidence, EvidenceAdmin)