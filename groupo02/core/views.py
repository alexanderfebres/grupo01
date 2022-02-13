
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import Specialist, Client, Appointment
from .serializers import SpecialistSerializer, ClientSerializer, AppointmentSerializer


class SpecialistListView(ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Specialist.objects.filter()
    serializer_class = SpecialistSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "user": ['exact'],
        "first_name": ['exact'],
        "last_name": ['exact'],
        "identifier_number": ['exact'],
        "birth_date": ['exact', 'gt', 'gte', 'lte', 'lt'],
    }
    search_fields = [
        "$user",
        "$first_name",
        "$last_name",
        "$identifier_number",
    ]


class SpecialistDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Specialist.objects.filter()
    serializer_class = SpecialistSerializer


class ClientListView(ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Client.objects.filter()
    serializer_class = ClientSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "user": ['exact'],
        "first_name": ['exact'],
        "last_name": ['exact'],
        "identifier_number": ['exact'],
        "birth_date": ['exact', 'gt', 'gte', 'lte', 'lt'],
    }
    search_fields = [
        "$user",
        "$first_name",
        "$last_name",
        "$identifier_number",
    ]


class ClientDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Client.objects.filter()
    serializer_class = ClientSerializer


class AppointmentListView(ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Appointment.objects.filter()
    serializer_class = AppointmentSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "specialist": ["exact"],
        "specialist__user": ["exact"],
        "specialist__identifier_number": ["exact"],
        "client": ["exact"],
        "client__user": ["exact"],
        "client__identifier_number": ["exact"],
        "title": ["exact"],
        "message": ["exact"],
        "answer": ["exact"],
        "appointment_type": ["exact"],
        "start_date": ['exact', 'gt', 'gte', 'lte', 'lt'],
        "attention_date": ['exact', 'gt', 'gte', 'lte', 'lt'],
    }
    search_fields = [
        "$specialist__user",
        "$specialist__identifier_number",
        "$client__user",
        "$client__identifier_number",
        "$title",
        "$message",
        "$answer",
    ]


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Appointment.objects.filter()
    serializer_class = AppointmentSerializer
