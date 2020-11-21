from django import forms
from .tasks import send_mail_task


# класс форм, не связанных с моделью
class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def form_valid(self, form):
        # print(form.cleaned_data)
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['message']
        email = form.cleaned_data['email']
        send_mail_task.delay(subject, text, email)
        return super().form_valid(form)

# # класс форм, связанных с моделью
# class SnakeForm(forms.ModelForm):
#     pass
