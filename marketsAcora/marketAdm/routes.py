from rest_framework import routers
from django.conf.urls import url,include
from appmarket.api import resources

router =routers.DefaultRouter()
router.register(r'Clients',resources.ClientsViewset,'ClientsList')
router.register(r'Markets',resources.MarketsViewset,'MarketsList')
router.register(r'Sections',resources.SectionsViewset,'SectionsList')
router.register(r'Points',resources.PointsViewset,'PointsList')
router.register(r'Concession',resources.ConcessionViewset,'ConcessionList')
router.register(r'Services',resources.ServicesViewset,'ServicesList')
router.register(r'Voucher',resources.VoucherViewset,'VoucherList')
router.register(r'VoucherDetail',resources.VoucherDetailViewset,'VoucherDetailList')
router.register(r'Msec',resources.MarketSectViewset,'MsecList')

urlpatterns = [
    url(r'^', include(router.urls)),
]
