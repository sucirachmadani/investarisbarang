from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventaris.models import Peminjaman, Barang
from .serializer import PeminjamanSerializer, BarangSerializer
from django.http import Http404
import os


class PeminjamanAPIView(APIView):
    def get(self, request):
        peminjaman = Peminjaman.objects.all()
        serializer = PeminjamanSerializer(peminjaman, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeminjamanSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            if instance.surat_permohonan:
                try:
                    surat_path = os.path.abspath(instance.surat_permohonan.path)
                    print(f"Surat permohonan disimpan di: {surat_path}")
                except Exception as e:
                    print(f"Gagal mendapatkan path file: {e}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeminjamanDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Peminjaman.objects.get(pk=pk)
        except Peminjaman.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        peminjaman = self.get_object(pk)
        serializer = PeminjamanSerializer(peminjaman)
        return Response(serializer.data)

    def put(self, request, pk):
        peminjaman = self.get_object(pk)
        serializer = PeminjamanSerializer(peminjaman, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        peminjaman = self.get_object(pk)
        serializer = PeminjamanSerializer(peminjaman, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        peminjaman = self.get_object(pk)
        peminjaman.delete()
        return Response(
            {"message": "Data berhasil dihapus"},
            status=status.HTTP_200_OK 
        )
    

class BarangListAPIView(APIView):
    def get(self, request):
        barang = Barang.objects.all()
        serializer = BarangSerializer(barang, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BarangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarangDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Barang.objects.get(pk=pk)
        except Barang.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        barang = self.get_object(pk)
        serializer = BarangSerializer(barang)
        return Response(serializer.data)

    def put(self, request, pk):
        barang = self.get_object(pk)
        serializer = BarangSerializer(barang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        barang = self.get_object(pk)
        serializer = BarangSerializer(barang, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        barang = self.get_object(pk)
        barang.delete()
        return Response({"message": "Barang berhasil dihapus"}, status=status.HTTP_200_OK)
