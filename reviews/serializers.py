from rest_framework import serializers
from .models import Review, Question, Answer, Choice
from django.db.models import Count


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'text'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'text',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    choice = ChoiceSerializer(read_only=True)
    
    class Meta:
        model = Answer
        fields = [
            'question',
            'choice'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    def get_answers(self, obj):
        answer = Answer.objects.filter(review=obj.id)
        response = AnswerSerializer(answer, many=True).data
        return response, {"count" : len(response)}
    class Meta:
        model = Review
        fields = [
            'submitted_at',
            'answers',
        ]

class ReviewCountSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    def get_answers(self, obj):
        answer = Answer.objects.filter(review=obj.id)
        response = AnswerSerializer(answer, many=True).data
        return {"count" : len(response)}
    class Meta:
        model = Review
        fields = [
            'submitted_at',
            'answers',
        ]

class AnswerCountSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    count = serializers.IntegerField()
    
    # def get_count(self, object):
    #     return len(object)
    
    class Meta:
        model = Answer
        fields = [
            'review',
            'count'
        ]
