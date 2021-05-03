from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    # name = serializers.CharField(max_length=100)
    # slug = serializers.CharField(max_length=100)
    # date = serializers.DateField()

    # def create(self,validated_data):
    #     return Event.objects.create(**validated_data)

    # def update(self,instance,validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.slug = validated_data.get('slug',instance.slug)
    #     instance.date = validated_data.get('date',instance.date)

    #     instance.save()
    #     return instance