from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/teste.html", context)

def create_poll(request):
    return HttpResponse("You're at the polls creator.")

def retrieve_poll(request):
    return HttpResponse("You're at the polls retrieve.")

def update_poll(request):
    return HttpResponse("You're at the polls update.")

def delete_poll(request):
    return HttpResponse("You're at the polls delete.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # A linha acima faz o mesmo que o try abaixo
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

