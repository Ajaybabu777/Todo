
from django.contrib import admin
from django.urls import path,include
from .views import home
from todo_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),

    # ToDo
    path('todos/', include('todos.urls'))
]
