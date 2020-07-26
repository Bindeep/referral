from django.contrib import admin
from .models import Country, Province, District, City

admin.site.register([
    Country, Province, District, City
])
