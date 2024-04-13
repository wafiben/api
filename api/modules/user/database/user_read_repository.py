from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from api.modules.user.commands.create_user.user_request_serializer import UserRequestSerializer
from .user_model import  User

class ReadUserRepository:
    def get_all_users(self):
        users = User.objects.all()
        serialized_users = list(users.values())
        return serialized_users
    
    def get_user_by_id(self, user_id):
            user = get_object_or_404(User,pk=user_id)
            serialized_user = model_to_dict(user) 
            return serialized_user
    
 