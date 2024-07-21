from django.urls import path, include
from core.views import *
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm


app_name = "core"

urlpatterns = [
    path('', home, name='home'),  # Корневой URL

    # Тестовые маршруты
    path('index/',index, name="index"),
    path('<int:my_id>/',indexItem, name="detail"),
    path('additem/', add_item, name="add_item"),

    path('register/', register, name='register'),

    #path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    #path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),

    #path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    #path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),

    path('login/', LoginView.as_view(template_name='core/login.html', authentication_form=CustomAuthenticationForm), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
]