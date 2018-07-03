from django.shortcuts import render,HttpResponse
from .models import concession, voucher,voucherDetail

# Create your views here.

def index(request):
    data = {}
    data['home'] = 'active'
    return render(request, 'index.html', {'menu': data, })

def admin(request):
    conseciones=concession.objects.all()
    data = {'conseciones':conseciones}
    return render(request, 'app/list-markets.html', data)

def vouchers(request):
    voucher_data=voucherDetail.objects.all()
    data = {'voucher':voucher_data}
    return render(request, 'app/list-vouchers.html', data)

def last_id_voucher(request):
    id = voucher.objects.latest('id')
    return HttpResponse(id.id)

def imprimir(request,id):
    #voucher= voucher.objects.filter(id=id).first()
    voucher_data = voucher.objects.filter(id=id).first()
    voucher_detail=voucherDetail.objects.filter(vouch=id).first()
    data = {'voucher':voucher_data,'voucherDetail':voucher_detail}
    return render(request, 'imprimir.html', data)

def water_reading(request):
    conseciones = concession.objects.all()
    data = {'conseciones': conseciones}
    return render(request, 'app/list-water-reading.html', data)

def electricity_reading(request):
    conseciones = concession.objects.all()
    data = {'conseciones': conseciones}
    return render(request, 'app/list-electricity-reading.html', data)