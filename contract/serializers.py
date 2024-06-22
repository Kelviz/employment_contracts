from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import Serializer, CharField
from .models import EmploymentAgreement



class UserSerializer(serializers.ModelSerializer):
    #Serialize django default user
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(Serializer):
    username = CharField(required=True)
    password = CharField(required=True)



class EmploymentAgreementSerializers(serializers.ModelSerializer):
        #Serialize EmploymentAgreement Model
        class Meta:
                model = EmploymentAgreement
                fields = "__all__"

        def validate(self, data):
                start_date = data.get('start_date')
                end_date = data.get('end_date')
                
                if start_date and end_date and start_date >= end_date:
                        raise serializers.ValidationError("The start date must be before the end date.")                       
                return data