from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_page(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)

def login_page(request):

    context = {
        
    }

    return render(request, 'accounts/login.html', context)

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'delivered': delivered,
        'total_orders': total_orders,
        'pending': pending,
    }

    return render(request, 'accounts/dashboard.html', context=context)

def product(request):

    product_list = Product.objects.all()

    p = Paginator(Product.objects.all(), 2)
    page = request.GET.get('page')
    products = p.get_page(page)

    context = {
        'product_list': product_list,
        'products': products,
    }

    return render(request, 'accounts/product.html', context)

def customer(request, pk_test):

    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'my_filter': my_filter,
    }

    return render(request, 'accounts/customer.html', context)

def create_order(request):

    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')


    context = {
        'form': form,
    }

    return render(request, 'accounts/order_form.html', context)

def update_order(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            
            return redirect('/')


    context = {
        'form': form,
    }

    return render(request, 'accounts/order_form.html', context)

def delete_order(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item': order
    }

    return render(request, 'accounts/delete.html', context)