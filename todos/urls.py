from django.urls import path
from .import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('markas_done/<int:pk>/',views.markas_done,name='markas_done'),
    path('markas_undone/<int:pk>/',views.markas_undone,name='markas_undone'),
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task')

]

