from django.urls import path
from .views import todoList, todoDetail

urlpatterns = [
    path('list/', todoList.as_view()),
    path('detail/', todoDetail.as_view()),
]
