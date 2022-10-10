from rest_framework import serializers
from sumari.models import Sumari

class SumariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sumari
        fields = '__all__'