from django.shortcuts import get_object_or_404
from api.modules.user.commands.create_user.user_request_serializer import UserRequestSerializer
from .user_model import  User

class WriteUserRepository:
    def create_user(self, user_data):
        user = User.objects.create(
            firstName=user_data['firstName'],
            lastName=user_data['lastName'],
            age=user_data['age'],
            gender=user_data['gender'],
            city=user_data['city']
        )
        return user
    
    def delete_user(user_id):
        try:
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return True  
        except User.DoesNotExist:
            return False 
  