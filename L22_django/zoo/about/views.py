from django.shortcuts import render


def about_view(request):
    print(request.method)
    return render(request, 'about/about.html')
