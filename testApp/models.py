from django.db import models

class Feedback(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField()
    # PERBAIKAN DI SINI: Gunakan auto_now_add=True
    tanggal_kirim = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback dari {self.nama}"