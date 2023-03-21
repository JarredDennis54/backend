from rest_framework import filters,generics
from .models import Categories
from .serializers import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset=Categories.objects.all()
    serializer_class =CategorySerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    
    

