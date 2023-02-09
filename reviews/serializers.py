from rest_framework import serializers
from .models import Review, Question, Answer, Choice


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'submitted_at'
        ]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'text'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(read_only=True)
    text = serializers.CharField(max_length=200)
    
    class Meta:
        model = Question
        fields = [
            'text',
            'choices'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)
    choice = ChoiceSerializer(read_only=True)
    
    class Meta:
        model = Answer
        fields = [
            'review',
            'question',
            'choice'
        ]