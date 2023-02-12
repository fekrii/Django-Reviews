from rest_framework import serializers
from .models import Review, Question, Answer, Choice



class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'text'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(read_only=True, many=True)
    class Meta:
        model = Question
        fields = [
            'text',
            'choices'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    # review = ReviewSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)
    choice = ChoiceSerializer(read_only=True)
    
    class Meta:
        model = Answer
        fields = [
            # 'review',
            'question',
            'choice'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    def get_answer(self, obj):
        answer = Answer.objects.filter(review=obj)
        response = AnswerSerializer(answer, many=True).data
        return response
    class Meta:
        model = Review
        fields = [
            'submitted_at',
            'answer'
        ]
