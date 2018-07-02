from rest_framework import serializers
from appmarket import models

class Clientsserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.clients
        fields = ('id','firstname','lastname','dni','cellphone','email')

class Marketsserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.markets
        fields = ('id', 'name')

class Sectionsserializer(serializers.HyperlinkedModelSerializer):
    markets = serializers.PrimaryKeyRelatedField(many=False, queryset=models.markets.objects.all())
    class Meta:
        model = models.sections
        fields = ('id','markets','name')


class Pointsserializer(serializers.HyperlinkedModelSerializer):
    sections= serializers.PrimaryKeyRelatedField(many=False, queryset=models.sections.objects.all())
    class Meta:
        model = models.points
        fields = ('id','sections','point_code','description')

class Concessionserializer(serializers.HyperlinkedModelSerializer):
    clients= serializers.PrimaryKeyRelatedField(many=False, queryset=models.clients.objects.all())
    points= serializers.PrimaryKeyRelatedField(many=False, queryset=models.points.objects.all())
    class Meta:
        model = models.concession
        fields = ('id', 'clients', 'points', 'date_consession_start', 'date_consession_end', 'price_monthly', 'point_name','sale_type')

class Servicesserializer(serializers.HyperlinkedModelSerializer):
    concession = serializers.PrimaryKeyRelatedField(many=False, queryset=models.concession.objects.all())
    class Meta:
        model = models.services
        fields = ('id','concession','service_water_read_old','service_water_read_new','service_water_price','service_energy_read_old','service_energy_read_new','service_energy_price')

class Voucherserializer(serializers.HyperlinkedModelSerializer):
    consession= serializers.PrimaryKeyRelatedField(many=False, queryset=models.concession.objects.all())

    class Meta:
        model = models.voucher
        fields = ('id', 'consession', 'date_pay', 'comments')

class VoucherDetailserializer(serializers.HyperlinkedModelSerializer):

    vouch=serializers.PrimaryKeyRelatedField(many=False, queryset=models.voucher.objects.all())
    class Meta:
        model = models.voucherDetail
        fields = ('id','vouch','price_point','price_water','price_energy')

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        models=models.markets
        fields = ('id', 'name')

class MerkSectSerializer(serializers.ModelSerializer):
    markets=MarkSerializer(many=True)
    class Meta:
        models=models.sections
        fields = ('id', 'name','markets')




    