import factory 
from reviews.models import Review, Choice, Question, Answer
from faker import Faker





fake = Faker()



## create Review Model Record 
class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review
        
    submitted_at = "2021-1-1"


## create Choice Model Record 
class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice
        
    text = "sample_choice"


## create question Model Record 
class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
        
    text = "sample_question"

    # Many-To-Many relation
    @factory.post_generation
    def choices(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for choice in extracted:
                self.choices.add(choice)


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer
        
    review = factory.SubFactory(ReviewFactory)
    question = factory.SubFactory(QuestionFactory)
    choice = factory.SubFactory(ChoiceFactory)
    
