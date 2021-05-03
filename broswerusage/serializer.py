from rest_framework import serializers
from .models import BroswerUsage

class BroswerUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroswerUsage
        fields = '__all__'