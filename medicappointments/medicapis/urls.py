from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'typeofvisits', views.TypeOfVisitViewSet)
router.register(r'medics', views.MedicViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'visits', views.VisitViewSet)
router.register(r'appointments', views.AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]




