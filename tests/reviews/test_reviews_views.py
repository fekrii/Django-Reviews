from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()


def test_review_get():
    request = factory.get('/reviews/')
    assert True
