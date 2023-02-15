import pytest

def test_review_str(review):
    assert review.__str__() == "2021-1-1"


def test_choice_str(choice):
    assert choice.__str__() == "sample_choice"


def test_question_str(question):
    assert question.__str__() == "sample_question"



def test_answer_str(answer):
    assert answer.__str__() == "Answer for question: ( sample_question )"