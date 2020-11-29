from django.urls import path
from .views import status_view # index_view
from .views import SnakesListView, ContactFormView, SnakesDetailView, SnakesCreateView,\
    SnakesUpdateView, SnakesDeleteView, UserCreateView, LoginUserView, LogoutUserView

app_name = 'snakes'

urlpatterns = [
    # path('', index_view, name='index'),
    path('', SnakesListView.as_view(), name='index'),
    path('registry/', UserCreateView.as_view(), name='registry'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('create/', SnakesCreateView.as_view(), name='create'),
    path('snake/<int:pk>/update/', SnakesUpdateView.as_view(), name='update'),
    path('snake/<int:pk>/delete/', SnakesDeleteView.as_view(), name='delete'),
    path('snake/<int:pk>/', SnakesDetailView.as_view(), name='snake_detail'),
    path('status/', status_view, name='status'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
