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

########################################



class settings_waterAdmin(admin.ModelAdmin):
    search_fields = ['id', 'price_water']
    list_display = ('id', 'price_water')

class settings_electricityAdmin(admin.ModelAdmin):
    search_fields = ['id', 'price_electricity']
    list_display = ('id', 'price_electricity')

class water_readingAdmin(admin.ModelAdmin):
    search_fields = ['id', 'consession','settings_water','service_water_read_old','service_water_read_new']
    list_display = ('id', 'consession','settings_water','service_water_read_old','service_water_read_new')

class electricity_readingAdmin(admin.ModelAdmin):
    search_fields = ['id', 'consession', 'settings_electricity', 'service_energy_read_old', 'service_energy_read_new']
    list_display = ('id', 'consession', 'settings_electricity', 'service_energy_read_old', 'service_energy_read_new')

class invoice_waterAdmin(admin.ModelAdmin):
    search_fields = ['id', 'water_reading', 'date_pay', 'comments','price_water']
    list_display = ('id', 'water_reading', 'date_pay', 'comments','price_water')

class invoice_electricityAdmin(admin.ModelAdmin):
    search_fields = ['id', 'electricity_reading', 'date_pay', 'comments', 'price_energy']
    list_display = ('id', 'electricity_reading', 'date_pay', 'comments', 'price_energy')


admin.site.register(models.clients,ClientsAdmin)
admin.site.register(models.markets,MarketsAdmin)
admin.site.register(models.sections,SectionsAdmin)
admin.site.register(models.points,PointsAdmin)
admin.site.register(models.concession,ConcessionAdmin)
admin.site.register(models.services,ServicesAdmin)
admin.site.register(models.voucher,VoucherAdmin)
admin.site.register(models.voucherDetail,VoucherDetailAdmin)

admin.site.register(models.settings_electricity,settings_electricityAdmin)
admin.site.register(models.settings_water,settings_waterAdmin)
admin.site.register(models.water_reading,water_readingAdmin)
admin.site.register(models.electricity_reading,electricity_readingAdmin)
admin.site.register(models.invoice_water,invoice_waterAdmin)
admin.site.register(models.invoice_electricity,invoice_electricityAdmin)



