from django.contrib import admin

from . import models


class QuestionInline(admin.TabularInline):
    model = models.Question.answers.through
    extra = 0
    min_num = 1


class PollInline(admin.TabularInline):
    model = models.Poll.questions.through
    extra = 0
    min_num = 1


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'answer',)
    search_fields = ('pk', 'answer',)
    empty_value_display = '-empty-'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'right_answer')
    exclude = ('answers',)
    search_fields = ('pk', 'question', 'answers__answer', 'right_answer__id')
    empty_value_display = '-empty-'
    inlines = (QuestionInline,)


class PollAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price')
    exclude = ('questions',)
    search_fields = ('pk', 'title', 'questions_question', 'price')
    empty_value_display = '-empty-'
    inlines = (PollInline,)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'price', 'login_color', 'bg_color',)
    search_fields = ('pk', 'price', 'login_color', 'bg_color',)
    empty_value_display = '-empty-'


class PassedPollAdmin(admin.ModelAdmin):
    list_display = ('pk', 'poll', 'user',)
    search_fields = ('pk', 'poll__title', 'user__email',)
    empty_value_display = '-empty-'


admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.PassedPoll, PassedPollAdmin)
