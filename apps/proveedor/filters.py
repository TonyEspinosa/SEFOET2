import django_filters

from .models import *

#Para incluir or
from django.db.models import Q

class ProvFilTer(django_filters.FilterSet):
    qs = django_filters.CharFilter(method='filter_qs')

    def filter_qs(self, qs, name, value):
        return qs.filter(
            Q(nombre__icontains=value) | Q(descripcion__icontains=value)
            )

class ProveedorFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label=' Nombre')
    descripcion = django_filters.CharFilter(lookup_expr='icontains', label=' Descripción')
    contacto = django_filters.CharFilter(lookup_expr='icontains', label=' Contacto')

    class meta:
        model = m_proveedor
        fields = ['nombre', 'descripcion', 'contacto']
    
    #def filter_qs(self, qs, name, value):
    #    return qs.filter(
    #        Q(nombre__icontains=value) | Q(descripcion__icontains=value)
    #        )
        #groups = [
        #    CombinedGroup(filters=['first_name', 'last_name'], combine=operator.or_),
        #]