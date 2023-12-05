from django.contrib import admin
from .models import Regiao, Prato, Usuario
from django.contrib.auth.admin import UserAdmin

# Este código somente existe porque desejamos que o campo
# personalisado Regioes_vistos seja exibido no sistema
# de administração do django
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('regioes_vistas',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Regiao)
admin.site.register(Prato)
admin.site.register(Usuario, UserAdmin)
