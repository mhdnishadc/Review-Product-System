# urls.py
from django.urls import path
from .views import ProductCreateView, ProductDetailView, ProductListView

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('products-list/', ProductListView.as_view(), name='product-list'),  #
]
