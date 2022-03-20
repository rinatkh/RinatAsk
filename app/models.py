from django.contrib.auth.models import UserManager
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    birth_date = models.DateField()

    objects = UserManager()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class QuestionManager(models.Manager):
    def one_question(self, id):
        return self.filter(id=id)

    def sorted_by_likes(self):
        return self.order_by('like__number')

    def get_questions_from_tag(self, id):
        return self.filter(tag=id)


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    tag = models.ManyToManyField('Tags')

    objects = QuestionManager()

    def __str__(self):
        return ' '.join({self.title, self.author.name})

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class AnswerManager(models.Manager):
    def one_question(self, id):
        return self.filter(id=id)

    def get_answers_by_question(self, id):
        return self.filter(question_id=id)


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = AnswerManager()

    def __str__(self):
        return ' '.join({self.text, self.author.name})

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class Tags(models.Model):
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Like(models.Model):
    number = models.IntegerField(default=0)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

# команда: python manage.py makemigrations
# >> python manage.py migrate

# python manage.py createsuperuser // работа с админ панелью

# Работа с бд
# >>python manage.py dbshell
# >> select * from catalog_author;
# >>.tables (просмотр моделей)

# создание новой формы из кода
# >> python manage.py shell
#  Book
# from catalog.models import Author
# author_2 = Author(first_name="An", last_name="chec")
# author_2.save()
# authors=Author.objects.all()
# authors.filter(first_name='Anton') - вывод толкьо Антонов
# print(authors.query) - выовд всех авторов
# authors.filter(birth_date__gt=datetime.data(2021,1,1) - вывод всех кто родился старше указанной даты
# authors.filter(birth_date__lt=datetime.data(2021,1,1) - вывод всех кто родился младше указанной даты
# authors.filter(birth_date__null=True) - вывод всех e кого нет даты рождения
# print(authors.filter(birth_date__null=True).query) - просмотреть запрос к бд
# authors_to_create = [Author(first_name=f"AuthorName#{1}", last_name=f"AuthorLastName#{1}") for i in range(100)] - создание авторов, но без вызова save.
#                                                                                                                   нужно каждую сохранить отдельно
# лучше использовать
# Author.object.bulk_create(authors_to_create).query

#

# >>.exit
