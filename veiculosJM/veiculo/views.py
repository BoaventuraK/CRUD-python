from django.shortcuts import render, redirect
from .models import Automovel

# Create your views here.
def home(request):
    aut = Automovel.objects.all()
    return render(request, 'home.html', {"aut": aut})

def salvar(request):
    tipo = request.POST.get("tipo")
    cor = request.POST.get("cor")
    marca = request.POST.get("marca")
    modelo = request.POST.get("modelo")
    estado = request.POST.get("estado")
    leilao = request.POST.get("leilao")
    f_pagamento = request.POST.get("f_pagamento")
    ano = request.POST.get("ano")
    km_rodado = request.POST.get("km_rodado")
    Automovel.objects.create(tipo=tipo, cor=cor, marca=marca, modelo=modelo, estado=estado, leilao=leilao, f_pagamento=f_pagamento, ano=ano, km_rodado=km_rodado)
    # Automovel.objects.create(cor=cor)
    # Automovel.objects.create(marca=marca)
    # Automovel.objects.create(modelo=modelo)
    # Automovel.objects.create(estado=estado)
    # Automovel.objects.create(leilao=leilao)
    # Automovel.objects.create(f_pagamento=f_pagamento)
    # Automovel.objects.create(ano=ano)
    # Automovel.objects.create(km_rodado=km_rodado)
    aut = Automovel.objects.all()
    return render(request, "home.html", {"aut": aut})

def editar(request, id):
    aut = Automovel.objects.get(id=id)
    return render(request, "update.html", {"auto": aut})

def update(request, id):
    tipo = request.POST.get("tipo")
    cor = request.POST.get("cor")
    marca = request.POST.get("marca")
    modelo = request.POST.get("modelo")
    estado = request.POST.get("estado")
    leilao = request.POST.get("leilao")
    f_pagamento = request.POST.get("f_pagamento")
    ano = request.POST.get("ano")
    km_rodado = request.POST.get("km_rodado")
    aut = Automovel.objects.get(id=id)
    aut.tipo = tipo
    aut.cor = cor
    aut.marca = marca
    aut.modelo = modelo
    aut.estado = estado
    aut.leilao = leilao
    aut.f_pagamento = f_pagamento
    aut.ano = ano
    aut.km_rodado = km_rodado
    aut.save()
    return redirect(home)

def delete(request, id):
    aut = Automovel.objects.get(id=id)
    aut.delete()
    return redirect(home)