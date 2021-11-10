from django.contrib import admin
from app.models import Profile, Question, Answer, Tags, Like

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tags)
admin.site.register(Like)