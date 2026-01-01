from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="homepage"),
    path('details/<int:taskID>', views.detailpage, name="detailpage"),
    path('taskpage/', views.createtaskform, name="taskpage")
]
