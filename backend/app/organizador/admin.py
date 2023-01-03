from django.contrib import admin

from .models import Cliente, Licenca, Condicionante, Medicoes

admin.site.register(Cliente)
admin.site.register(Licenca)
admin.site.register(Condicionante)
admin.site.register(Medicoes)
