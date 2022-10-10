from django.db.models.signals import post_save
from django.dispatch import receiver

from applications.polls import models


@receiver(post_save, sender=models.PassedPoll)
def user_balance_sum(instance, **kwargs):
    poll_price = instance.poll.price
    new_user_balance = instance.user.balance + poll_price
    instance.user.balance = new_user_balance
    instance.user.save()


@receiver(post_save, sender=models.PassedPoll)
def user_passed_polls(instance, **kwargs):
    instance.user.passed_test_quantity += 1
    instance.user.save()
