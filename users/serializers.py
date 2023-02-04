from rest_framework import serializers
from .models import User,Movies,Cast


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast  
        fields = '__all__'         

class MoviesSerializer(serializers.ModelSerializer):
    cast = CastSerializer(read_only=True, many=True)
    class Meta:
        model = Movies  
        fields = '__all__'         