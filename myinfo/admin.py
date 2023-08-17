from django.contrib import admin
from myinfo.models import Survey, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display=("username", "survey_idx", "answer_idx")
class SurveyAdmin(admin.ModelAdmin):
    list_display=("question", "ans1", "ans2", "ans3", "ans4", "ans5", "status")

# Register your models here.

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer, AnswerAdmin)