from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.modules.user.database.user_model import User
from api.modules.user.database.user_read_repository import ReadUserRepository




class GetSingleUserController:
    @staticmethod
    def get_single_user(request, user_id):
        readUserRepository=ReadUserRepository()
        user =readUserRepository.get_user_by_id(user_id)
        return JsonResponse({'user': user})
    