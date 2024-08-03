from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from forms import ProductForm, ProductModelForm

from online_shop.models import Category, Product


# Create your views here.





def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'online_shop/home.html', context)

class AddProduct(View):
    def get(self, request):
        form = ProductModelForm()
        return render(request, 'online_shop/home.html', {'form': form})

    def post(self, request):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

class EditProduct(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        form = ProductModelForm(instance=product)
        return render(request, 'online_shop/home.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        form = ProductModelForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk)

class ProductDelete(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if product:
            product.delete()
            return redirect('index')
