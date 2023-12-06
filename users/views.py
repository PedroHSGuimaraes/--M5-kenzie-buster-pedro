from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication, InvalidToken
from rest_framework.views import APIView, Request, Response, status
from users.permissions import VerifyPermissionOrder
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [VerifyPermissionOrder]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)

        if request.user.id == user_id or request.user.is_employee:
            serializer = UserSerializer(user)

            return Response(serializer.data, status.HTTP_200_OK)

        return Response(
            {"detail": "Você não tem permissão para realizar esta ação."},
            status.HTTP_403_FORBIDDEN,
        )

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)

        if request.user.id == user_id or request.user.is_employee:
            serializer = UserSerializer(user, data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(serializer.data, status.HTTP_200_OK)

        return Response(
            {"detail": "Você não tem permissão para realizar esta ação."},
            status.HTTP_403_FORBIDDEN,
        )
