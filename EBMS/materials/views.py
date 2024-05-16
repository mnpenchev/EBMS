from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MaterialSerializer
from .permissions import IsAdminOrSupply
from .models import Material


class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSupply]


class MaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSupply]
