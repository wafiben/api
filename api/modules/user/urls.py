from django.urls import path
from .queries.get_all_users.get_all_users_controller import GetUsersController

urlpatterns = [
    path('', GetUsersController.get_users, name='get_all_users'),
]