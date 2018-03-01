from django.contrib import admin
from .models import event
from .models import register, sa
# Register your models here.
admin.site.register(event)
admin.site.register(register)
admin.site.register(sa)
