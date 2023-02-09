from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Review, Question, Answer, Choice
from .serializers import ReviewSerializer, QuestionSerializer, AnswerSerializer, ChoiceSerializer

class ReviewList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
