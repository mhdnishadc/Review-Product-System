# views.py
from rest_framework import generics
from .models import product
from .serializers import ProductSerializer

# Create Product
class ProductCreateView(generics.CreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, Update, Delete Product (by ID)
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'  # use 'pk' if you're using default

class ProductListView(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None  # Disable pagination if not needed
