from http import client
from rest_framework import serializers

from .models import Specialist, Client, Appointment


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            'pk',
            'user',
            'first_name',
            'last_name',
            'birth_date',
            'identifier_number',
            'state',
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'pk',
            'user',
            'first_name',
            'last_name',
            'birth_date',
            'identifier_number',
            'state',
        )


class AppointmentSerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer(read_only=True)
    specialist_id = serializers.IntegerField(write_only=True)

    client = ClientSerializer(read_only=True)
    client_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Appointment
        fields = (
            'pk',
            'specialist',
            'specialist_id',
            'client',
            'client_id',
            'title',
            'message',
            'answer',
            'start_date',
            'attention_date',
            'appointment_type',
            'state'
        )
