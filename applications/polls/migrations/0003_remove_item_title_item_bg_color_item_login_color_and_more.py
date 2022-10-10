# Generated by Django 4.1.2 on 2022-10-09 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
        migrations.AddField(
            model_name='item',
            name='bg_color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет фона'),
        ),
        migrations.AddField(
            model_name='item',
            name='login_color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет логина'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=255, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='passedpoll',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passed_polls', to='polls.poll', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='passedpoll',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passed_polls', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Баллы>'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='questions',
            field=models.ManyToManyField(related_name='polls', to='polls.question', verbose_name='Вопросы'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(related_name='questions_wa', to='polls.answer', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='right_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions_ra', to='polls.answer', verbose_name='Верный ответ'),
        ),
    ]
