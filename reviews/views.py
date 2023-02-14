from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Review, Question, Answer, Choice
from .serializers import ReviewSerializer, QuestionSerializer, AnswerSerializer, ChoiceSerializer, AnswerCountSerializer
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination


class ReviewView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self, *args, **kwargs):
        oldest_date = Review.objects.latest('-submitted_at')
        latest_date = Review.objects.latest('submitted_at')
        from_date = self.request.GET.get('from', str(oldest_date))
        to_date = self.request.GET.get('to',str(latest_date))
        review = super().get_queryset(*args, **kwargs).filter(submitted_at__gte=from_date, submitted_at__lte=to_date).annotate(Count('submitted_at', distinct=True))
        return review


class AnswersCountView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    def get_queryset(self, *args, **kwargs):
        oldest_date = Review.objects.latest('-submitted_at')
        latest_date = Review.objects.latest('submitted_at')
        from_date = self.request.GET.get('from', str(oldest_date))
        to_date = self.request.GET.get('to',str(latest_date))
        answers = super().get_queryset(*args, **kwargs).filter(review__submitted_at__gte=from_date, review__submitted_at__lte=to_date).annotate(Count('review', distinct=True))
        return answers
        