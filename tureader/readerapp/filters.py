import django_filters
from .models import Reader




class ReaderFilter(django_filters.FilterSet):


    class Meta:
        model = Reader
        fields = {
            'rank':['icontains'],
            'phd':['icontains'],
        }
