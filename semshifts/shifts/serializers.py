from rest_framework import serializers
from .models import Shift


class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ('driver', 'clock_in', 'clock_out', 'km_driven', 'shift_length')

