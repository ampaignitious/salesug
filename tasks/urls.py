from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="homepage"),
    path('details/<int:taskID>', views.detailpage, name="detailpage"),
    path('taskpage/', views.createtaskform, name="taskpage"),
    path('deletetask/<int:taskID>', views.deletetask, name="deletetask"),
    path('edittask/<int:taskID>', views.edittask, name="edittask")
]
