from django import forms
from .tasks import send_mail_task
from .models import Snake
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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

# класс форм, связанных с моделью
class SnakeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Snake # связываем форму с моделью
        exclude = ('user', )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your password',
    }))

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username' : forms.TextInput(attrs={'placeholder':'John Gault', 'class':'col-md-12form-control'}),
                   'email' : forms.EmailInput(attrs={'placeholder':'your@mail.com', 'class':'col-md-12form-control'}),
                   }

class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'