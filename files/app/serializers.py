"""
Serializers for app
"""
from rest_framework import serializers

from .models import Game, Publisher, Developer, Salestime, Nation, Region


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer class for Game model
    """

    class Meta:
        model = Game
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializer class for Game model
    """

    class Meta:
        model = Publisher
        fields = '__all__'


class DeveloperSerializer(serializers.ModelSerializer):
    """
    Serializer class for Game model
    """

    class Meta:
        model = Developer
        fields = '__all__'


class SalestimeSerializer(serializers.ModelSerializer):
    """
    Serializer class for Salestime model
    """

    class Meta:
        model = Salestime
        fields = '__all__'

class NationSerializer(serializers.ModelSerializer):
    """
    Serializer class for Nation model
    """

    class Meta:
        model = Nation
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    """
    Serializer class for Region model
    """

    class Meta:
        model = Region
        fields = '__all__'
