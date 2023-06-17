from rest_framework.serializers import ModelSerializer
from ..models import HeatData


class HeatDataSerializer(ModelSerializer):
    class Meta:
        model = HeatData
        fields = '__all__'
