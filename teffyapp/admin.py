from django.contrib import admin
from teffyapp.models import *
# Register your models here.
admin.site.register([PersonalInformation,UserProfile,SalesPurchases])