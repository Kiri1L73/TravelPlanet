from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product
from products.models import ProductImage


def site2(request):
    name = "Khasanov"
    current_day = "22.03.2023"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing.html', locals())


def home(request):

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_hot_tur =  products_images.filter(product__category_id=2)
    products_images_beach_tur = products_images.filter(product__category_id=4)
    return render(request, 'home.html', locals())

# Create your views here.
