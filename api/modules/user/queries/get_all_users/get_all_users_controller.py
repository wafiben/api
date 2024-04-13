from django.http import JsonResponse
from yaml import serialize

from api.modules.user.database.user_model import User
from api.modules.user.database.user_read_repository import ReadUserRepository

class GetUsersController:
    @staticmethod
    def get_users(request):
        readUserRepository = ReadUserRepository()
        users = readUserRepository.get_all_users()
        return JsonResponse({"users": users})
    



    