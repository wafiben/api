from django.http import JsonResponse

class GetSingleUserController:
    @staticmethod
    def get_users(request):
        return JsonResponse({"message": "single user querie"})