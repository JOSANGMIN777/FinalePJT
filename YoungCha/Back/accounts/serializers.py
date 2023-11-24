from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()




class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    age = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['age'] = self.validated_data.get('age', '')

        return data
    
    def save(self, request):
        user = super().save(request)
        user.nickname = self.data.get('nickname')
        user.age = self.data.get('age')
        user.save()
        return user
    



class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = UserDetailsSerializer.Meta.extra_fields
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('username', 'email', )