from django.contrib import admin
from .models import Reservation, Table
# Register your models here.


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'number',
        'capacity'
    ]
    list_display_links = [
        'id',
        'number'
    ]
    search_fields = [
        'number',
    ]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'table',
        'reserved_at',
        'duration_hours',
    ]
    search_fields = [
        'user__email',
        'user__username',
        'table__number'
    ]
    list_filter = ['reserved_at', 'table']
    list_display_links = [
        'id',
        'table',
    ]


    

admin.site.site_header = "Panel de Administración – Reservas"
admin.site.site_title = "Admin Reservas"
admin.site.index_title = "Bienvenido al panel de reservas"