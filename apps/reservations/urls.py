from rest_framework.routers import DefaultRouter
from .views import TableViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'reservations', ReservationViewSet, basename='reservations')

urlpatterns = router.urls