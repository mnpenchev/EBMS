from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='products'),
]