from django.shortcuts import render
from django.core.paginator import Paginator

answers_in_question = [
    {
        "title_in_answer": f"Title of answer {i}",
        "text_in_answer": f"This is text for {i} question.",
    } for i in range(20)
]

questions = [
    {
        "title": f"Title {i}",
        "text": f"This is text for {i} question.",
        "number": i,
        "answers": answers_in_question,
    } for i in range(100)
]

def index(request):
    paginator = Paginator(questions, 7)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {"questions": content})


def hot(request):
    paginator = Paginator(questions, 7)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", {"questions": content})


def question(request, number):
    paginator = Paginator(questions[number]["answers"], 7)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "question.html", {"questions": content})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def settings(request):
    return render(request, "settings.html")