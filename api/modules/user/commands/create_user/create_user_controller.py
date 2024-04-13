import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.modules.user.database.user_write_repository import WriteUserRepository
from .user_request_serializer import UserRequestSerializer


class CreateUserController:
    @staticmethod
    @csrf_exempt
    def create_user(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            serializer = UserRequestSerializer(data=data)
            if serializer.is_valid():
                WriteUserRepository().create_user(data)
                return JsonResponse({"message":"sucess"}, status=201)
            else:
                return JsonResponse({"errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)
