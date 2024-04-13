from django.urls import path,include
from api.modules.user.commands.delete_user.delete_user_controller import DeleteUserController
from api.modules.user.commands.modify_user.modify_user_controller import ModifyUserController
from api.modules.user.queries.get_all_users.get_all_users_controller import GetUsersController
from api.modules.user.commands.create_user.create_user_controller import CreateUserController
from api.modules.user.queries.get_single_user.get_single_user_controller import GetSingleUserController

urlpatterns = [
     path('users',GetUsersController.get_users, name='get_all_users'),
     path('create_user',CreateUserController.create_user, name='create_user'),
     path('users/<int:user_id>', GetSingleUserController.get_single_user, name='get_single_user'),
     path('delete_user/<int:user_id>', DeleteUserController.delete_user, name='delete_user_by_id'),
     path('modify_user/<int:user_id>', ModifyUserController.modify_user, name='modify_user'),
]
