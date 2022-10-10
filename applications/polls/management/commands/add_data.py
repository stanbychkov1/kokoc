import csv
import os

from django.core.management import BaseCommand
from django.db import connection
from django.db.models import Max

from applications.polls import models
from kokoc import settings


def correct_sequence_value(model, field='id', conn=connection):
    max_id = model.objects.aggregate(max_id=Max(field))['max_id'] or 1
    cursor = conn.cursor()
    cursor.execute(
        "SELECT setval(pg_get_serial_sequence(%s,%s),%s)", (
            model._meta.db_table,
            model._meta.get_field(field).column,
            max_id,
        ))


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Добавление ответов
        if models.Answer.objects.all().count() != 0:
            return 'All answers have already been created before'
        with open(
                os.path.join(settings.BASE_DIR, 'test_data/answers.csv'),
                encoding='utf-8',
        ) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                answer = models.Answer.objects.create(
                    id=row[0],
                    answer=row[1], )
                print(f'Answer {answer.id} created')
        correct_sequence_value(models.Answer)

        # Добавление вопросов
        if models.Question.objects.all().count() != 0:
            return 'All questions have already been created before'
        with open(
                os.path.join(settings.BASE_DIR, 'test_data/questions.csv'),
                encoding='utf-8',
        ) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                question = models.Question.objects.create(
                    id=row[0],
                    question=row[1],
                    right_answer_id=row[3])
                ids = row[2].split(',')
                answers = models.Answer.objects.filter(pk__in=ids)
                for answer in answers:
                    question.answers.add(answer)
                print(f'Question {question.id} created')
        correct_sequence_value(models.Question)

        # Добавление опросов
        if models.Poll.objects.all().count() != 0:
            return 'All polls have already been created before'
        with open(
                os.path.join(settings.BASE_DIR, 'test_data/polls.csv'),
                encoding='utf-8',
        ) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                poll = models.Poll.objects.create(
                    id=row[0],
                    title=row[1],
                    price=row[3])
                ids = row[2].split(',')
                questions = models.Question.objects.filter(pk__in=ids)
                for question in questions:
                    poll.questions.add(question)
                print(f'Poll {poll.id} created')
        correct_sequence_value(models.Poll)

        # Добавление предложений
        if models.Item.objects.all().count() != 0:
            return 'All items have already been created before'
        with open(
                os.path.join(settings.BASE_DIR, 'test_data/items.csv'),
                encoding='utf-8',
        ) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                item = models.Item.objects.create(
                    id=row[0],
                    price=row[1],
                    login_color=row[2],
                    bg_color=row[3], )
                print(f'Item {item.id} created')
        correct_sequence_value(models.Item)
