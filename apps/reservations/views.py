from rest_framework import viewsets, permissions
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer
from rest_framework.exceptions import ValidationError
from datetime import timedelta

# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    query = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAdmin]

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        table = serializer.validated_data['table']
        start = serializer.validated_data['reserved_at']
        end = start + timedelta(hours=serializer.validated_data['duration_hours'])

        overlapping = Reservation.objects.filter(
            table=table,
            reserved_at__lt=end,
            reserved_at__gte=start - timedelta(hours=table.capacity)
        )

        if overlapping.exists():
            raise ValidationError('La mesa no esta disponible en ese horario.')
        
        serializer.save(user=self.request.user)
