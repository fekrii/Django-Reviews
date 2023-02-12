from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Review, Question, Answer, Choice
from .serializers import ReviewSerializer, QuestionSerializer, AnswerSerializer, ChoiceSerializer

# class ReviewList(generics.ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


class ReviewList(APIView):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all().first()
        reviewsdistinct = Review.objects.all().values('submitted_at').annotate(Count('user__device', distinct=True))

        print('fekri---------------', reviewsdistinct)
        serializer = ReviewSerializer(reviews)
        return Response({
            'success': True,
            'data': serializer.data
        })