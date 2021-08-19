from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from app.models import CustomUser
from .serializers import UserDetailSerializer
from rest_framework import permissions

# Create your views here.
class UserDetail(ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return CustomUser.objects.filter(self.request.user)

class UserDetailDo(RetrieveDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return CustomUser.objects.filter(self.request.user)