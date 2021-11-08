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

tags = [
    {'id': 0, 'text': 'perl'},
    {'id': 1, 'text': 'Python'},
    {'id': 2, 'text': 'MySQL'},
    {'id': 3, 'text': 'Technopark'},
    {'id': 4, 'text': 'Django'},
    {'id': 5, 'text': 'MailRU'},
    {'id': 6, 'text': 'FireFox'},
    {'id': 7, 'text': 'Psycho'}
]


def index(request):
    content = paginate(questions, request, 7)
    return render(request, "index.html", {"questions": content})


def hot(request):
    content = paginate(questions, request, 7)
    return render(request, "hot.html", {"questions": content})


def question(request, number):
    content = paginate(answers_in_question, request, 7)
    return render(request, "question.html", {"que": questions[number], "questions": content})


def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def settings(request):
    return render(request, "settings.html")


def tag(request, id):
    content = paginate(questions, request, 7)
    return render(request, "tag.html", {"tag": tags[id], "questions": content})


def paginate(objects_list, request, per_page):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return page
