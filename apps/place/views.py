from rest_framework import filters,generics
from .models import Place
from .serializers import PlaceSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class PlaceList(generics.ListAPIView):
    queryset=Place.objects.all()
    serializer_class =PlaceSerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'place_type']
    search_fields =[ 'name','description']

# Create your views here.
