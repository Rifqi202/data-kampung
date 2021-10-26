from django.db import models
from django.shortcuts import redirect, render

from . import models
# Create your views here.
def index(request):
    return render(request, "index.html")
# def login(request):
#     if request.POST:
#         input_NIK = request.POST["NIK"]
#         input_password = request.POST["password"]
#         user = models.login.objects.filter(NIK = input_NIK, password= input_password).first()
        
#         if user is not None:

#     return redirect('/')
#     return render(request, "login.html")

def daftarwarga(request):
    if request.POST:
        input_nama = request.POST["nama"]
        input_NIK = request.POST["NIK"]
        input_TTL = request.POST["TTL"]
        input_pekerjaan = request.POST["pekerjaan"]
    models.daftarwarga.objects.create(nama = input_nama, NIK = input_NIK, TTL = input_TTL, pekerjaan = input_pekerjaan)
    data = models.daftarwarga.objects.all()
    return render(request, "index.html",{
        "data": data,
    })


    
