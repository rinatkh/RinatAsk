from django.core.management.base import BaseCommand
from app.models import Question, Profile, Tags, Answer
from random import choice
from faker import Faker

f = Faker()


class Command(BaseCommand):


    def fill_users(self, cnt):
        for i in range(cnt):
            print(i)
            Profile.objects.create(
                name=f.name(),
                birth_date=f.date()
            )


    def fill_tags(self, cnt):
        for i in range(cnt):
            print(i)
            Tags.objects.create(
                designation=f.word()
            )


    def fill_questions(self, cnt):
        users_ids = list(
            Profile.objects.values_list(
                'id', flat=True
            )
        )
        tags_ids = list(
            Tags.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            print(i)
            qst = Question.objects.create(
                author_id=choice(users_ids),
                text='. '.join(f.sentences(f.random_int(min=2, max=5))),
                title=f.sentence()[:128],
            )
            for i in range(f.random_int(min=0, max=15)):
                qst.tag.add(tags_ids[f.random_int(min=0, max=len(tags_ids)-1)])


    def fill_answers(self, cnt):
        users_ids = list(
            Profile.objects.values_list(
                'id', flat=True
            )
        )
        qst_ids = list(
            Question.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            print(i)
            Answer.objects.create(
                author_id=choice(users_ids),
                text='. '.join(f.sentences(f.random_int(min=2, max=5))),
                question_id=choice(qst_ids)
            )
[]

