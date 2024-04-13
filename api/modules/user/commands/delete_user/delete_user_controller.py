from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from api.modules.user.database.user_model import User

class DeleteUserController:
    @staticmethod
    @csrf_exempt
    def delete_user(request, user_id):
        if request.method == 'DELETE':
            try:
                user = get_object_or_404(User, id=user_id)
                user.delete()
                return JsonResponse({'message': 'User deleted successfully'}, status=204)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
