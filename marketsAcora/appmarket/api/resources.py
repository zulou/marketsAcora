from rest_framework import viewsets
from appmarket import models
from . import serializers

class ClientsViewset(viewsets.ModelViewSet):
	queryset=models.clients.objects.all()
	serializer_class=serializers.Clientsserializer

class MarketsViewset(viewsets.ModelViewSet):
    queryset = models.markets.objects.all()
    serializer_class = serializers.Marketsserializer

class SectionsViewset(viewsets.ModelViewSet):
    queryset = models.sections.objects.all()
    serializer_class = serializers.Sectionsserializer

class PointsViewset(viewsets.ModelViewSet):
    queryset = models.points.objects.all()
    serializer_class = serializers.Pointsserializer

class ConcessionViewset(viewsets.ModelViewSet):
    queryset = models.concession.objects.all()
    serializer_class = serializers.Concessionserializer

class ServicesViewset(viewsets.ModelViewSet):
    queryset = models.services.objects.all()
    serializer_class = serializers.Servicesserializer

class VoucherViewset(viewsets.ModelViewSet):
    queryset = models.voucher.objects.all()
    serializer_class = serializers.Voucherserializer

class VoucherDetailViewset(viewsets.ModelViewSet):
    queryset = models.voucherDetail.objects.all()
    serializer_class = serializers.VoucherDetailserializer

class MarketSectViewset(viewsets.ModelViewSet):
    queryset = models.voucherDetail.objects.all()
    serializer_class = serializers.Marketsserializer

##
class Settings_waterViewset(viewsets.ModelViewSet):
    queryset = models.settings_water.objects.all()
    serializer_class = serializers.Settings_waterSerializer

class Settings_electricityViewSet(viewsets.ModelViewSet):
    queryset = models.settings_electricity.objects.all()
    serializer_class = serializers.Settings_electricitySerializer

class Water_readingViewset(viewsets.ModelViewSet):
    queryset = models.water_reading.objects.all()
    serializer_class = serializers.Water_readingSerializer

class Electricity_readingViewset(viewsets.ModelViewSet):
    queryset = models.electricity_reading.objects.all()
    serializer_class = serializers.Electricity_readingSerializer

class Invoice_waterViewset(viewsets.ModelViewSet):
    queryset = models.invoice_water.objects.all()
    serializer_class = serializers.Invoice_waterSerializer

class Invoice_electricityViewset(viewsets.ModelViewSet):
    queryset = models.invoice_electricity.objects.all()
    serializer_class = serializers.Invoice_electricitySerializer









