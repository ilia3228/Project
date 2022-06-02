import datetime
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product,ProductInstance

def index(request):
    value = 0
    context = {
        'value': value,
    }
    return render(request, 'catalog/index.html', context=context)

class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10


class ProductInstanceDetailView(generic.DetailView):
    model = ProductInstance
