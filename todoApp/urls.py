from django.urls import path
from .views import todoList, todoDetail, todoCreate, todoDelete, todoUpdate

urlpatterns = [
    path('list/', todoList.as_view(), name='list'),
    path('detail/<int:pk>', todoDetail.as_view(), name='detail'),
    path('create/', todoCreate.as_view(), name='create'),
    path('delete/<int:pk>', todoDelete.as_view(), name='delete'),
    path('update/<int:pk>', todoUpdate.as_view(), name='update')
]
