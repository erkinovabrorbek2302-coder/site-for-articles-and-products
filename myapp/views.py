from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from myapp.models import Maqola, Mahsulot


def home(request):
    return render(request, 'home.html')


def maqola_list(request):
    maqolalar = Maqola.objects.all()
    return render(request, 'maqola_list.html', {'maqolalar': maqolalar})


def maqola_detail(request, pk):
    maqola = get_object_or_404(Maqola, id=pk)
    return render(request, 'maqola_detail.html', {'maqola': maqola})


def mahsulot_list(request):
    mahsulotlar = Mahsulot.objects.all()
    return render(request, 'mahsulot_list.html', {'mahsulotlar': mahsulotlar})


def mahsulot_detail(request, slug):
    mahsulot = get_object_or_404(Mahsulot, slug=slug)
    return render(request, 'mahsulot_detail.html', {'mahsulot': mahsulot})


def maqola_search(request):
    qidiruv = request.GET.get('nom', '')
    if qidiruv:
        natijalar = Maqola.objects.filter(nom__icontains=qidiruv)
    else:
        natijalar = Maqola.objects.all()
    return render(request, 'maqola_search.html', {'natijalar': natijalar, 'qidiruv': qidiruv})

def api_maqolalar(request):
    maqolalar = Maqola.objects.all()
    date = []
    for maqola in maqolalar:
        date.append({
            'id': maqola.pk,
            'nom': maqola.nom,
            'muallifi': maqola.muallifi,
            'sarlavha': maqola.sarlavha,
            'tavsif': maqola.tavsif,
        })
        return JsonResponse(date, safe=False)
