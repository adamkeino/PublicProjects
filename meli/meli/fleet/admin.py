from django.contrib import admin

from .models import Vehicle
from .models import Driver

admin.site.register(Vehicle)
admin.site.register(Driver)
