from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserRegistrationForm, UserForm


class SignUp(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial = {}
        for field in UserForm().fields:
            value = getattr(self.request.user, field)
            initial[field] = value
        context['form'] = UserForm(initial=initial,
                                   disable_fields=True)
        return context


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'profile.html'
    form_class = UserForm
    success_url = reverse_lazy('success')

    def get_object(self, queryset=None):
        return self.request.user
