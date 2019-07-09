from rest_framework import serializers

from .models import Record, OneRecord


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'name', 'status', 'expire_at', 'max_hash_length', 'num_links')


class OneUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OneRecord
        fields = ('long_url', 'max_hash_length', 'expiration_time')


class KeysSerializer(serializers.Serializer):
    key = serializers.CharField(required=False, allow_blank=True, max_length=100)
