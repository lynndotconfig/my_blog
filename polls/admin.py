"""Register model for polls admin."""
from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    """Question Admin."""

    fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
