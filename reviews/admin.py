from django.contrib import admin
from .models import Review, Choice, Question, Answer

admin.site.register(Review)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Answer)

