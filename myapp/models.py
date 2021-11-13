from django.contrib.auth.models import User
from django.db import models


class QuizModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_question = models.IntegerField()
    corrent_question = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def total(self):
        return round((100 * self.corrent_question) / self.total_question, 2)