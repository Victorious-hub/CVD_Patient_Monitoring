from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from apps.users.permissions import IsDoctor, IsPatient
from rest_framework_simplejwt.tokens import RefreshToken


class UserLogoutAPi(views.APIView):
    permission_classes = (IsDoctor | IsPatient,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
