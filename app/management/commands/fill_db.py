from django.core.management.base import BaseCommand
from app.models import Qstion, User, Tags, Answer
from random import choice
from faker import Faker

f = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.fill_users(options['users'])
        self.fill_tags(options['tags'])
        self.fill_questions(options['questions'])
        self.fill_answers(options['answers'])

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--users',
            action='store',
            dest='users',
            type=int
        )
        parser.add_argument(
            '-t',
            '--tags',
            action='store',
            dest='tags',
            type=int
        )
        parser.add_argument(
            '-q',
            '--questions',
            action='store',
            dest='questions',
            type=int
        )
        parser.add_argument(
            '-a',
            '--answers',
            action='store',
            dest='answers',
            type=int
        )


    def fill_users(self, cnt):
        for i in range(cnt):
            User.objects.create(
                name=f.name(),
                birth_date=f.date()
            )


    def fill_tags(self, cnt):
        for i in range(cnt):
            Tags.objects.create(
                designation=f.word()
            )


    def fill_questions(self, cnt):
        users_ids = list(
            User.objects.values_list(
                'id', flat=True
            )
        )
        tags_ids = list(
            Tags.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            qst = Qstion.objects.create(
                author_id=choice(users_ids),
                text='. '.join(f.sentences(f.random_int(min=2, max=5))),
                title=f.sentence()[:128],
            )
            for i in range(f.random_int(min=0, max=15)):
                qst.tag.add(tags_ids[f.random_int(min=0, max=len(tags_ids)-1)])


    def fill_answers(self, cnt):
        users_ids = list(
            User.objects.values_list(
                'id', flat=True
            )
        )
        qst_ids = list(
            Qstion.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            Answer.objects.create(
                author_id=choice(users_ids),
                text='. '.join(f.sentences(f.random_int(min=2, max=5))),
                question_id=choice(qst_ids)
            )


