import csv
import io
from random import shuffle, sample

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Question, Answer, Result, QuizModel

def qiuz(request):
    quizs = QuizModel.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'quiz.html', context)


@login_required(login_url='login')
def quistion(request, pk):
    quistions = Question.objects.filter(quiz_id = pk)
    quistions = sample(list(quistions), 2)
    answers = Answer.objects.all()
    answers = list(answers)
    shuffle(answers)
    if request.method == "POST":
        correct = 0
        wrong = 0
        for q in quistions:
            if request.POST.get(q.name) == "True":
                correct += 1
            else:
                wrong += 1
            quiz = q.quiz
        Result.objects.create(
            user=User.objects.get(username=request.user.username),
            total_question=len(quistions),
            corrent_question=correct,
            quiz = quiz
        )
        context = {
            'correct': correct,
            'wrong': wrong,
            'total_question': len(quistions),
            'user': request.user.username,
            'total': round(correct * 100 / len(quistions), 2)
        }
        return render(request, 'result.html', context)
    context = {
        'quistions': quistions,
        'answers': answers,
    }

    return render(request, 'quistion.html', context)

def users_upload(request):
    users = User.objects.all()
    if request.method == "POST":
        csv_file = request.FILES['users']
        file_data = csv_file.read().decode("utf-8")
        io_string = io.StringIO(file_data)
        next(io_string)
        for row in csv.reader(io_string, delimiter=','):
            User.objects.create_user(first_name=row[0], last_name=row[1],
                                     username=row[2], password=row[3],
                                     email=row[4])

    return render(request, 'users_upload.html', {'users':users})

def result_list(request):
    results = Result.objects.all()
    context = {
        'results': results
    }
    return render(request, 'result_list.html', context)