from django.urls import path
from core.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "core"

urlpatterns = [
    #path('api/', include(router.urls)),
    #path('export/csv/', export_records_csv),
    #path('export/pdf/', export_records_pdf),
    path('', home, name='home'),  # Корневой URL
    #path('doctor/mypatients/',doctor_page, name="mypatients"),
    #path('administrator/myusers/',admin_page, name="myusers"),

    # Тестовые маршруты
    path('index/',index, name="index"),
    path('<int:my_id>/',indexItem, name="detail"),
    path('additem/', add_item, name="add_item"),

    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
]