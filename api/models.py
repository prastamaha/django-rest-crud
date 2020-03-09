from django.db import models

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=10)
    nis = models.IntegerField()

    def __str__(self):
        return self.nama
    
class Tugas(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(f'{self.siswa} | {self.item}')

