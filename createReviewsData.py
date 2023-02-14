import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import random


import django 
django.setup() 

from faker import Faker 
from reviews.models import * 
from model_bakery.recipe import Recipe,foreign_key 


import datetime
start_date = datetime.date(year=2021, month=1, day=1)
end_date = datetime.date(year=2023, month=12, day=31)

fake = Faker() 

for k in range(4000):
    fake_date = fake.date_between(start_date=start_date, end_date=end_date)
    
    if Review.objects.filter(submitted_at=fake_date).exists():
        review = Review.objects.get(submitted_at=fake_date)
        question = Question.objects.get(id=random.randint(1,4))
        answer = Recipe(Answer, 
                    review=review,
                    question=question,
                    choice=random.choice(question.choices.all())) 
        answer.make()
        print("1", review)
    else:
        review=Recipe(Review, submitted_at=fake_date)
        question = Question.objects.get(id=random.randint(1,4))
        answer = Recipe(Answer, 
                    review=foreign_key(review),
                    question=question,
                    choice=random.choice(question.choices.all())) 
        answer.make()
        print("2", review)
