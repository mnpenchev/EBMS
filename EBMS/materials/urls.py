from django.urls import path
from .views import MaterialListCreateAPIView, MaterialRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', MaterialListCreateAPIView.as_view(), name='materials'),
    path('<int:pk>/', MaterialRetrieveUpdateDestroyAPIView.as_view(), name='material'),
]