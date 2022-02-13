from django.urls import path

from core.views import (AppointmentDetailView, AppointmentListView,
                        ClientDetailView, ClientListView, SpecialistDetailView,
                        SpecialistListView)

urlpatterns = [
    # Specialists
    path("specialists/", SpecialistListView.as_view(), name="specialists"),
    path("specialists/<int:pk>/", SpecialistDetailView.as_view(),
         name="specialists-detail"),

    # Clients
    path("clients/", ClientListView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientDetailView.as_view(),
         name="clients-detail"),

    # Appointments
    path("appointments/", AppointmentListView.as_view(), name="appointments"),
    path("appointments/<int:pk>/", AppointmentDetailView.as_view(),
         name="appointments-detail"),
]
