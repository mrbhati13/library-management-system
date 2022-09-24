from rest_framework import serializers
from .models import UserAccount

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email','password','user_type']