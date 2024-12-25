from django.contrib import admin
from .models import Buyer, Games, News

# Register your models here.

admin.site.register(News)

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_filter = ('size','cost',)  # Фильтрация по полям
    list_display = ('title','cost','size',)  # Поля для отображения в списке
    search_fields = ('title',)  # Поля для поиска
    list_per_page = 20  # Ограничение кол-ва записей, отображаемых на странице

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance','age',)
    list_display = ('name','balance','age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)
