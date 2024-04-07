from django.http import JsonResponse

class CreateUserController:
    @staticmethod
    def get_users(request):
        return JsonResponse({"message": "hello"})