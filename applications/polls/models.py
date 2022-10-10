from django.db import models

from django.contrib.auth import get_user_model


class Answer(models.Model):
    answer = models.CharField(max_length=255,  verbose_name='Ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.CharField(max_length=255,  verbose_name='Вопрос')
    answers = models.ManyToManyField(to=Answer,
                                     related_name='questions_wa',
                                     verbose_name='Ответы')
    right_answer = models.ForeignKey(to=Answer, null=True,
                                     on_delete=models.SET_NULL,
                                     related_name='questions_ra',
                                     verbose_name='Верный ответ')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class Poll(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    questions = models.ManyToManyField(to=Question, related_name='polls',
                                       verbose_name='Вопросы')
    price = models.PositiveIntegerField(default=0, verbose_name='Баллы>')

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Item(models.Model):
    price = models.PositiveIntegerField(default=0, verbose_name='Стоимость')
    login_color = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Цвет логина')
    bg_color = models.CharField(max_length=255, blank=True, null=True,
                                verbose_name='Цвет фона')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Цвет логина {self.login_color} и цвет фона {self.bg_color}'


class PassedPoll(models.Model):
    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE,
                             related_name='passed_polls',
                             verbose_name='Опрос')
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE,
                             related_name='passed_polls',
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Пройденный опрос'
        verbose_name_plural = 'Пройденные опросы'
