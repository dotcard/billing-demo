from django.shortcuts import render, get_object_or_404
from billing.models import Customer

def index(request):
  customers_list = Customer.objects.order_by('-lname')
  context = {'customers_list' : customers_list}
  return render(request, 'billing/index.html', context)

def detail(request, customer_id):
  cust = get_object_or_404(Customer, pk = customer_id)
  context = {'cust' : cust}
  return render(request, 'billing/detail.html', context)
