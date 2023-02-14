from django.urls import path
from .views import ReviewView, AnswersCountView

urlpatterns = [
    path('reviews/', ReviewView.as_view()),
    path('answers_count/', AnswersCountView.as_view()),
    
]