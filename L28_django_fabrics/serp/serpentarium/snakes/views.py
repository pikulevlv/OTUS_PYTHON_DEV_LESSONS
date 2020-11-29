from django.core.mail import send_mail
from django.shortcuts import render
from .models import Snake
import time
from .tasks import save_snakes, send_mail_task
from celery import current_app
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from .forms import ContactForm, SnakeForm, RegistrationForm, AuthenticationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        # просто сформулировать условие выдачи прав
        # return self.request.user.email.endswith('@example.com')
        return self.request.user.is_superuser

class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class SnakesListView(ListView):
    model = Snake # Модель, которую нужно вывести в список
    template_name = 'snakes/index.html' # в какой шаблон выведем данные

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '1'
        return context

class SnakesDetailView(DetailView):
    model = Snake
    template_name = 'snakes/snake_detail.html'

class SnakesCreateView(StaffOnlyMixin, CreateView):
    model = Snake
    template_name = 'snakes/edit_create.html'
    success_url = '/'
    # fields = '__all__' # возьмем все поля
    # fields = ('name','card', 'specia', 'age') # перечислим нужные поля
    # исключить ненужные поля можно в формах
    form_class = SnakeForm

    def form_valid(self, form):
        user = self.request.user # мы т.к. в форме создания змеи скрывали пользователя
        form.instance.user = user # прописываем его из инстанса формы
        return super().form_valid(form) # сохраняем форму


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'snakes/register.html'


class SnakesUpdateView(StaffOnlyMixin, UpdateView):
    model = Snake
    template_name = 'snakes/edit_create.html'
    success_url = '/'
    # fields = '__all__' # возьмем все поля
    form_class = SnakeForm



class SnakesDeleteView(AdminOnlyMixin, DeleteView):
    model = Snake
    template_name = 'snakes/delete_confirm.html'
    success_url = '/'

# def index_view(request):
#     # snakes = Snake.objects.all()
#     snakes = Snake.objects.select_related('specia__family').all()
#     # snakes = Snake.objects.prefetch_related('specia__family').all()
#     context = {"snakes": snakes}
#     if request.method == 'POST':
#         # print(time.time())
#         # save_snakes.delay()
#         # print(time.time())
#         result = send_mail_task.delay('celery_topic', 'celery_text')
#         context['task_id'] = result.id
#
#     return render(request, 'snakes/index.html', context)

def status_view(request):
    task_id = request.GET['task_id']
    # status = 'done'
    task = current_app.AsyncResult(task_id)
    status = task.status
    # status = None
    
    context = {"status": status, "task_id": task_id}
    return render(request, "snakes/status.html", context)

# only for auth users
class ContactFormView(LoginRequiredMixin, FormView):
    template_name = "snakes/contact.html"
    form_class = ContactForm
    success_url = '/'


class LoginUserView(LoginView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'snakes/login.html'


class LogoutUserView(LogoutView):
    pass


