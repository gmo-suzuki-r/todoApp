from django.urls import path
from .views import todoList, todoDetail, todoCreate

urlpatterns = [
    path('list/', todoList.as_view()),
    path('detail/<int:pk>', todoDetail.as_view()),
    path('create/', todoCreate.as_view()),
]
