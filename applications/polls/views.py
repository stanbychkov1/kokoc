from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from applications.polls import models, forms

User = get_user_model()


class IndexView(LoginRequiredMixin, generic.ListView):
    model = models.Poll
    template_name = 'index.html'

    def get_queryset(self):
        return models.Poll.objects.exclude(
            passed_polls__user_id=self.request.user.id
        )


class PollView(LoginRequiredMixin, PermissionRequiredMixin,
               FormMixin, generic.DetailView):
    model = models.Poll
    template_name = 'poll.html'
    success_url = reverse_lazy('success')

    def has_permission(self):
        poll = self.get_object()
        polls = models.Poll.objects.filter(
            passed_polls__user_id=self.request.user.id)
        if poll in polls:
            return False
        return True

    def get_form(self, **kwargs):
        formset = forms.QuestionFormSet(queryset=self.object.questions.all())
        return formset

    def post(self, request, *args, **kwargs):
        formset = forms.QuestionFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)
        return self.form_invalid(formset)

    def form_valid(self, formset):
        user = self.request.user
        poll = self.get_object()
        passed_poll = models.PassedPoll(
            user=user,
            poll=poll
        )
        passed_poll.save()
        return super().form_valid(formset)

    def form_invalid(self, formset):
        return HttpResponseRedirect(reverse_lazy('unsuccess'))


class SuccessView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'misc/success.html'

    def get_context_data(self, **kwargs):
        referer = self.request.META.get('HTTP_REFERER')
        context = super(SuccessView, self).get_context_data(**kwargs)
        if 'unsuccess' in self.request.path and 'item' in referer:
            context['success'] = ('У вас недостаточно средств,'
                                  ' чтобы купить данное предложение')
            return context
        elif 'unsuccess' in self.request.path:
            context['success'] = (
                'К сожалению вы не ответили на все вопросы верно.'
                'Вы можете пройти тест заново или выбрать другой.')
            return context
        elif 'poll' in referer:
            context['success'] = 'Вы ответили на все вопросы верно.'
            return context
        elif 'me/update' in referer:
            context['success'] = 'Данные профиля обновлены.'
            return context
        elif 'item' in referer:
            context['success'] = 'Поздравлем с покупкой предложения.'
            return context
        return context


class RatingView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return User.objects.all().order_by('-passed_test_quantity')


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = models.Item
    template_name = 'index.html'


class ItemBuyView(LoginRequiredMixin, SingleObjectMixin, View):
    model = models.Item
    template_name = 'buy_item.html'

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        user_balance = self.request.user.balance
        if user_balance - item.price < 0:
            return HttpResponseRedirect(reverse_lazy('unsuccess'))
        if item.login_color:
            self.request.user.username_color = item.login_color
        if item.bg_color:
            self.request.user.background_color = item.bg_color
        self.request.user.balance -= item.price
        self.request.user.save()
        return HttpResponseRedirect(reverse_lazy('success'))
