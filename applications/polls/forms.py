from django import forms
from django.forms import modelformset_factory

from applications.polls import models


class PassedPollForm(forms.ModelForm):
    class Meta:
        model = models.PassedPoll
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    answers = forms.ModelChoiceField(queryset=None, label='Ответы',
                                     widget=forms.RadioSelect)

    class Meta:
        model = models.Question
        fields = ('answers',)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answers'].queryset = self.instance.answers.all()

    def is_valid(self):
        if self.cleaned_data['answers'].id == self.instance.right_answer_id:
            return super().is_valid()
        return False


QuestionFormSet = modelformset_factory(models.Question, form=QuestionForm,
                                       extra=0)
