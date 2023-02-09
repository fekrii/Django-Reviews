from django.db import models


class Review(models.Model):
    submitted_at = models.DateTimeField()
    


    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return str(self.submitted_at)
    
class Choice(models.Model):
    text = models.CharField(max_length=20)
    
    def __str__(self):
        return self.text

class Question(models.Model):
    text = models.TextField()
    choices = models.ManyToManyField(Choice, related_name='questions')
    
    def __str__(self):
        return self.text

class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Answer for question: ( {self.question.text} )'
    