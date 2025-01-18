from rest_framework import serializers

from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['name', 'slug', 'price', 'created', 'status', 'published', 'updated', 'id']
        read_only_fields = ['created', 'updated', 'id']