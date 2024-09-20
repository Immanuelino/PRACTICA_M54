# myapp/views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

class ProtectedListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'app1/my_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)

@login_required
def home(request):
    return render(request, 'app1/home.html')
