from rest_framework.serializers import ModelSerializer
from app.models import CustomUser

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'address']