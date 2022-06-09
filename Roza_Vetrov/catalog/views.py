import datetime
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect


def index(request):
    categories = Category.objects.all().annotate(count=Count('product')).order_by('-count')[:5]
    products = Product.objects.all().order_by('-id')[:6]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'catalog/index.html', context=context)


class ProductListView(models.Model, generic.ListView):
    model = Product

    def get_queryset(self):
        return super().get_queryset().annotate(items=Count('productinstance')) \
            .order_by('-items')

    paginate_by = 6


class ProductDetailView(generic.DetailView):
    model = Product


class CategoryListView(generic.ListView):
    model = Category


class CategoryDetailView(generic.DetailView):
    model = Category


class ProductInstanceDetailView(generic.DetailView):
    model = ProductInstance


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'  # Not recommended (potential security issue if more fields added)

    def form_valid(self, form):
        new = form.save()  # save form
        return redirect('product-detail', pk=new.pk)


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

    def form_valid(self, form):
        new = form.save()  # save form
        return redirect('category-detail', pk=new.pk)


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'  # Not recommended (potential security issue if more fields added)
    def form_valid(self, form):
        new = form.save()  # save form
        return redirect('category-detail', pk=new.pk)


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('products')
