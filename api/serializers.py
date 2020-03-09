from rest_framework import serializers
from .models import *

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'

class TugasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tugas
        fields = '__all__'