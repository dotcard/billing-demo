from django.contrib import admin
from billing.models import Customer
from billing.models import Tariff

class CustomerAdmin(admin.ModelAdmin):
  list_display = ('lname', 'fname', 'tariff')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tariff)
