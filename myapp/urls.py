# urls.py
from django.urls import path
from .views import ProductCreateView, ProductDetailView, ProductListView, RegisterView, LoginView, LogoutView, ReviewCreateView

urlpatterns = [
    #User
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),

    #Products
    path('products/create/', ProductCreateView.as_view(), name='product-create'),

    # Retrieve[GET], Update[PUT], Delete[DELETE] Product (by ID)
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('products-list/', ProductListView.as_view(), name='product-list'), 

    #Reviews
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),

]
