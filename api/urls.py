from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingByPatientView, MappingDeleteView,
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),

    # Patients
    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),

    # Doctors
    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),

    # Mappings
    path('mappings/', MappingListCreateView.as_view()),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view()),
    path('mappings/<int:pk>/delete/', MappingDeleteView.as_view()),
]
