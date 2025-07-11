from rest_framework import serializers
from inventaris.models import Peminjaman, Barang

class PeminjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peminjaman
        fields = '__all__'

    def create(self, validated_data):
        barang = validated_data.pop('barang')
        instance = Peminjaman.objects.create(barang=barang, **validated_data)
        return instance

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = '__all__'