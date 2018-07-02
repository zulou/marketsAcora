from django.contrib import admin
from appmarket import models

class ClientsAdmin(admin.ModelAdmin):
    search_fields = ['id','firstname','lastname','dni','cellphone','email']
    list_display = ('id','firstname','lastname','dni','cellphone','email')

class MarketsAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ('id', 'name')

class SectionsAdmin(admin.ModelAdmin):
    search_fields = ['id','markets','name']
    list_display = ('id','markets','name')

class PointsAdmin(admin.ModelAdmin):
    search_fields = ['id','sections','point_code','description']
    list_display = ('id','sections','point_code','description')

class ConcessionAdmin(admin.ModelAdmin):
    search_fields = ['id', 'clients', 'points', 'date_consession_start', 'date_consession_end', 'price_monthly', 'point_name']
    list_display = ('id', 'clients', 'points', 'date_consession_start', 'date_consession_end', 'price_monthly', 'point_name')

class ServicesAdmin(admin.ModelAdmin):
    search_fields = ['id','concession','service_water_read_old','service_water_read_new','service_water_price','service_energy_read_old','service_energy_read_new','service_energy_price']
    list_display = ('id','concession','service_water_read_old','service_water_read_new','service_water_price','service_energy_read_old','service_energy_read_new','service_energy_price')

class VoucherAdmin(admin.ModelAdmin):
    search_fields = ['id', 'consession', 'date_pay', 'comments']
    list_display = ('id', 'consession', 'date_pay', 'comments')

class VoucherDetailAdmin(admin.ModelAdmin):
    search_fields = ['id','vouch','price_point','price_water','price_energy']
    list_display = ('id','vouch','price_point','price_water','price_energy')


admin.site.register(models.clients,ClientsAdmin)
admin.site.register(models.markets,MarketsAdmin)
admin.site.register(models.sections,SectionsAdmin)
admin.site.register(models.points,PointsAdmin)
admin.site.register(models.concession,ConcessionAdmin)
admin.site.register(models.services,ServicesAdmin)
admin.site.register(models.voucher,VoucherAdmin)
admin.site.register(models.voucherDetail,VoucherDetailAdmin)


