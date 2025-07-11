from django.db import models

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    kode_barang = models.CharField(max_length=30, unique=True)
    jumlah = models.PositiveIntegerField()
    lokasi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama} ({self.kode_barang})"

class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('Dipinjam', 'Dipinjam'),
        ('Dikembalikan', 'Dikembalikan'),
    ]

    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    peminjam = models.CharField(max_length=100)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField(null=True, blank=True)
    surat_permohonan = models.FileField(upload_to='surat_permohonan/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Dipinjam')

    def __str__(self):
        return f"{self.peminjam} - {self.barang.nama} ({self.status})"
