from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register(r'typeofvisits', views.TypeOfVisitViewSet)
router.register(r'medics', views.MedicViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'visits', views.VisitViewSet)
router.register(r'appointments', views.AppointmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('appointmentsbymedic/', views.AppointmentsFilteredListByMedic.as_view()),
    path('appointmentsbypatient/', views.AppointmentsFilteredListByPatient.as_view()),
]
