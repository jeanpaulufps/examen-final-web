from rest_framework import viewsets
from .serializers import TableSerializer, ReservationSerializer
from .models import Table, Reservation

# Create your views here.
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer