from rest_framework import serializers

from accounts.serializers import UserPublicSerializer

from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']
    
    def get_uri(self,obj):
        return 'status/{id}'.format(id=obj.id)

    def validate(self,data):
        content = data.get('content',None)

        if content=="":
            content=None

        image = data.get('image',None)

        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required')
        
        return data
