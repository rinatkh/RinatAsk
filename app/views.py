from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import Profile, Question, Answer, Tags, Like

def index(request):
    context = paginate(Question.objects.all(), request, 7)

    return render(request, 'index.html', context)


def hot(request):
    context = paginate(Question.objects.all(), request, 7)
    return render(request, "hot.html", context)


def question(request, number):
    context = paginate(Answer.objects.get_answers_by_question(number), request, 7)
    context['question'] = Question.objects.get(id=number)
    return render(request, "question.html", context)


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def settings(request):
    return render(request, "settings.html")


def tag(request, id):
    context = paginate(Question.objects.get_questions_from_tag(id), request, 3)
    context['tag'] = Tags.objects.get(id=id)

    return render(request, "tag.html", context)


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
