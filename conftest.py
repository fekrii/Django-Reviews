import pytest
from pytest_factoryboy import register

from tests.factories import ReviewFactory, ChoiceFactory, QuestionFactory, AnswerFactory

register(ReviewFactory)
register(ChoiceFactory)
register(QuestionFactory)
register(AnswerFactory)




@pytest.fixture
def review(db, review_factory):
    review = review_factory.create()
    return review


@pytest.fixture
def choice(db, choice_factory):
    choice = choice_factory.create()
    return choice


@pytest.fixture
def question(db, question_factory):
    question = question_factory.create()
    return question


@pytest.fixture
def answer(db, answer_factory):
    answer = answer_factory.create()
    return answer