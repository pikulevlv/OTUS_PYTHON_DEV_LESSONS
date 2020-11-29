from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '1'
        return context

# def about_view(request):
#     context = {}
#     context['active_page'] = '1'
#     return render(request, 'about/about.html', context)