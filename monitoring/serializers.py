from rest_framework import serializers
from .models import Keyword,Flag

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name']

class FlagSerializer(serializers.ModelSerializer):
    keyword = serializers.StringRelatedField()
    content_item = serializers.StringRelatedField()

    class Meta:
        model = Flag
        fields = '__all__'           