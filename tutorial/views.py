from django.http import HttpResponse
from .models import Question
#from django.shortcuts import render
from django.template import loader

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #latestQuestionList = Question.objects.order_by('-pubDate')[:5]
    #output = ', '.join([q.questionText for q in latestQuestionList])
    #return HttpResponse(output)

    latestQuestionList = Question.objects.order_by('-pubDate')[:5]
    template = loader.get_template('tutorial/index.html')
    context = {
        'latestQuestionList': latestQuestionList,
    }
    return HttpResponse(template.render(context, request))

def detail(request, questionId):
    return HttpResponse("You're looking at question %s." % questionId)

def results(request, questionId):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)