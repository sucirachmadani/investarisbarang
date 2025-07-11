from django.urls import path
from .views import PeminjamanAPIView, PeminjamanDetailAPIView, BarangListAPIView, BarangDetailAPIView

urlpatterns = [
    path('peminjaman/', PeminjamanAPIView.as_view()),
    path('peminjaman/<int:pk>/', PeminjamanDetailAPIView.as_view()),
    path('barang/', BarangListAPIView.as_view()),
    path('barang/<int:pk>/', BarangDetailAPIView.as_view()),
]
