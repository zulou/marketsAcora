from django.db import models
from datetime import date,timedelta

# Create your models here.

class clients(models.Model):
    firstname=models.CharField(max_length=20, default="", blank=True)
    lastname=models.CharField(max_length=50, default="", blank=True)
    dni=models.CharField(default="", max_length=45, unique=True)
    cellphone=models.CharField(max_length=9, default="", blank=True)
    email=models.CharField(max_length=20, default="", blank=True)
    def __str__(self):
        return(str(self.firstname)+" "+str(self.lastname)+" "+str(self.dni)+" "+str(self.cellphone)+" "+str(self.email))

class markets(models.Model):
    name=models.CharField(max_length=20, default="", blank=True)
    def __str__(self):
        return(str(self.name))

class sections(models.Model):
    markets = models.ForeignKey(markets, on_delete=models.CASCADE,related_name="markets")
    name = models.CharField(max_length=20, default="", blank=True)
    def __str__(self):
        return(str(self.markets)+' '+str(self.name))

class points(models.Model):
    sections=models.ForeignKey(sections,on_delete=models.CASCADE,related_name="sections")
    point_code=models.CharField(max_length=20, default="", blank=True)
    description=models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return(str(self.sections)+" "+str(self.point_code)+" "+str(self.description))

class concession(models.Model):
    clients=models.ForeignKey(clients,on_delete=models.CASCADE,related_name="clients")
    points=models.ForeignKey(points,on_delete=models.CASCADE,related_name="points")
    date_consession_start=models.DateField(blank=False, default=date.today())
    date_consession_end=models.DateField(blank=True, default=date.today())
    sale_type = models.CharField(max_length=45, default="", blank=True)
    price_monthly=models.IntegerField(unique=False)
    point_name=models.CharField(max_length=45,default="",blank=True)
    def __str__(self):
        return(str(self.clients)+' '+str(self.points)+' '+str(self.date_consession_start)+' '+str(self.date_consession_end)+' '+str(self.price_monthly)+' '+str(self.point_name))
    def paid_days_concession(self):
        query_monto=self.concessions_voucher.all()

        suma=0
        test=None
        for val in query_monto:
            test=val.voucher_detail.values_list('price_point',flat=True).get()
            suma=suma+test
        return(int(suma))

    def total_days_concession(self):
        date_start = self.date_consession_start
        date_end = self.date_consession_end
        total_days = date_end - date_start
        return (str(total_days.days))

    def voucher_date(self):
        date_v=self.concessions_voucher.all()
        cad = []
        for date_e in date_v:
            cad.append(date_e.date_pay.isoformat())
        #list_result=[entry.isoformat() for entry in date_v]
        #cantidad_dias=timedelta(days=5)
        return(",".join(cad))

    def price_day(self):
        return (int(price_monthly / 30))

class services(models.Model):
    concession=models.ForeignKey(concession,on_delete=models.CASCADE,related_name="concessions_services")
    service_water_read_old=models.IntegerField(unique=False)
    service_water_read_new = models.IntegerField(unique=False)
    service_water_price = models.IntegerField(unique=False)
    service_energy_read_old = models.IntegerField(unique=False)
    service_energy_read_new = models.IntegerField(unique=False)
    service_energy_price = models.IntegerField(unique=False)
    def __str__(self):
        return(self.concession+" "+self.service_water_read_old+" "+self.service_water_read_new+" "+self.service_water_price+" "+self.service_energy_read_old+" "+self.service_energy_read_new+" "+self.service_energy_price)

class voucher(models.Model):
    consession=models.ForeignKey(concession,on_delete=models.CASCADE,related_name="concessions_voucher")
    date_pay=models.DateField(blank=True, default=date.today())
    comments=models.CharField(max_length=20, default="", blank=True)
    def __str__(self):
        return(str(self.consession)+" "+str(self.date_pay)+" "+str(self.comments))


class voucherDetail(models.Model):
    vouch=models.ForeignKey(voucher,on_delete=models.CASCADE,related_name="voucher_detail")
    price_point=models.IntegerField(unique=False)
    price_water=models.IntegerField(unique=False)
    price_energy= models.IntegerField(unique=False)
    def __str__(self):
        return(str(self.vouch)+" "+str(self.price_point)+" "+str(self.price_water)+" "+str(self.price_energy))

##################
class settings_water(models.Model):
    price_water=models.IntegerField(unique=False)

class settings_electricity(models.Model):
    price_electricity=models.IntegerField(unique=False)

class water_reading(models.Model):
    consession = models.ForeignKey(concession, on_delete=models.CASCADE, related_name="concessions_water_reading")
    settings_water=models.ForeignKey(concession, on_delete=models.CASCADE, related_name="water_reding_settings_water")
    service_water_read_old = models.IntegerField(unique=False)
    service_water_read_new = models.IntegerField(unique=False)

class electricity_reading(models.Model):
    consession = models.ForeignKey(concession, on_delete=models.CASCADE, related_name="concessions_electricity_reading")
    settings_electricity = models.ForeignKey(concession, on_delete=models.CASCADE, related_name="water_reding_settings_electricity")
    service_energy_read_old = models.IntegerField(unique=False)
    service_energy_read_new = models.IntegerField(unique=False)


class invoice_water(models.Model):
    water_reading=models.ForeignKey(water_reading,on_delete=models.CASCADE,related_name="water_reading_invoice_water")
    date_pay = models.DateField(blank=True, default=date.today())
    comments = models.CharField(max_length=20, default="Pago por agua", blank=True)
    price_water = models.IntegerField(unique=False)


class invoice_electricity(models.Model):
    electricity_reading= models.ForeignKey(electricity_reading, on_delete=models.CASCADE,related_name="electricity_reading_invoice_electricity")
    date_pay = models.DateField(blank=True, default=date.today())
    comments = models.CharField(max_length=20, default="pago por electricidad", blank=True)
    price_energy = models.IntegerField(unique=False)













