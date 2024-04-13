import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from api.modules.user.commands.create_user.user_request_serializer import UserRequestSerializer
from api.modules.user.database.user_model import User


class ModifyUserController:
    @staticmethod
    @csrf_exempt
    def modify_user(request, user_id):
        if request.method == 'PUT':
                user = get_object_or_404(User, id=user_id)
                data = json.loads(request.body)
                serializer = UserRequestSerializer(data=data)
                print(serializer.is_valid())
                if serializer.is_valid():
                    for key, value in data.items():
                        setattr(user, key, value)
                    user.save()  
                    return JsonResponse({'message': 'User updated successfully'}, status=200)




