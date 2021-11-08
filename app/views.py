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
    paginator = Paginator(answers_in_question, 7)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "question.html", {"que": questions[number], "questions": content})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def settings(request):
    return render(request, "settings.html")

def paginate(objects_list, request, per_page):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return context
