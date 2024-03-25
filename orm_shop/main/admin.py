from django.contrib import admin

# зарегистрируйте необходимые модели
from .models import Client
from .models import Car
from .models import Sale

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Sale)
