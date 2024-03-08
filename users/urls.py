from django.urls import path
from .views import home, profile, RegView

urlpatterns = [
    # Домашняя страница
    path('', home, name = 'home'),
    # Страница профиля
    path('profile/', profile, name = 'profile'),
    # Страница регистрации
    path('registration/', RegView.as_view(), name = 'registration'),
]
