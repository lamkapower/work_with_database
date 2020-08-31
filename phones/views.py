from django.shortcuts import render

from .models import Phone


def show_catalog(request):  
    return render(request, "catalog.html", {
        "phones": Phone.objects.all().order_by(request.GET.get('sort')) if request.GET.get('sort') is not None else Phone.objects.all()
        })


def show_product(request, slug):
    return render(request, "product.html", {"phone": Phone.objects.get(slug=slug)})
