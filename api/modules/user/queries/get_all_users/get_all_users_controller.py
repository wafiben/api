from django.http import JsonResponse

class GetUsersController:
    @staticmethod
    def get_users(request):
        return JsonResponse({"message": "hello"})