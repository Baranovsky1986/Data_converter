from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from location_register.models.ratu_models import Region, District, City, Citydistrict, Street
from location_register.serializers.ratu_serializers import RegionSerializer, DistrictSerializer, CitySerializer, CitydistrictSerializer, \
    StreetSerializer
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination


class CachedViewMixin:
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class RegionView(CachedViewMixin,viewsets.ReadOnlyModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
class DistrictView(CachedViewMixin, viewsets.ReadOnlyModelViewSet):
    pagination_class = PageNumberPagination
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class CityView(CachedViewMixin, viewsets.ReadOnlyModelViewSet):
    pagination_class = PageNumberPagination
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitydistrictView(CachedViewMixin, viewsets.ReadOnlyModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Citydistrict.objects.all()
    serializer_class = CitydistrictSerializer
    
class StreetView(CachedViewMixin, viewsets.ReadOnlyModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

