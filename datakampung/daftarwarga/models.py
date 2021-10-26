from django.db import models

# Create your models here.
# class login (models.Model):
#     NIK = models.IntegerField()
#     Password = models.CharField(max_length=200)

class daftarwarga (models.Model):
    nama = models.CharField(max_length=200)
    NIK = models.IntegerField()
    TTL = models. IntegerField()
    pekerjaan = models.CharField(max_length=200)
