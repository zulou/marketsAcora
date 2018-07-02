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









