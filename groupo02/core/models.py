from django.db import models


class AuditRecordFieldModelMixing(models.Model):
    _STATES = (
        ('A', 'A'),
        ('C', 'C'),
    )

    class Meta:
        verbose_name = ('AuditRecordFieldsModelMixing')
        abstract = True

    created = models.DateField(
        auto_now=True,
        verbose_name=("Created")
    )
    updated = models.DateField(
        auto_now=True,
        verbose_name=("Updated")
    )
    created_by = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=("Created By")
    )
    updated_by = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=("Updated By")
    )
    state = models.CharField(
        max_length=5,
        choices=_STATES,
        default='A',
        null=True,
        verbose_name=('State')
    )


class PersonModelMixing(models.Model):

    class Meta:
        verbose_name = ('PersonModelMixing')
        abstract = True

    user = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=('User')
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=('First Name')
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=('Last Name')
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=('Birth Date')
    )
    identifier_number = models.CharField(
        max_length=45,
        verbose_name=('Identifier Number')
    )

    def __str__(self):
        return self.first_name + self.last_name


class Specialist(PersonModelMixing, AuditRecordFieldModelMixing):
    class Meta:
        verbose_name = ('Specialist')
        verbose_name_plural = ('Specialists')


class Client(PersonModelMixing, AuditRecordFieldModelMixing):
    class Meta:
        verbose_name = ('Client')
        verbose_name_plural = ('Clients')


class Appointment(AuditRecordFieldModelMixing):
    _APPOINTMENT_STATE = (
        ('P', 'P'),
        ('A', 'A'),
    )

    class Meta:
        verbose_name = ('Appointment')
        verbose_name = ('Appointments')

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        verbose_name=('Specialist')
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=('Client')
    )
    title = models.CharField(
        max_length=250,
        verbose_name=('First Name')
    )
    message = models.TextField(
        verbose_name=('Message')
    )
    answer = models.TextField(
        verbose_name=('Answer')
    )
    start_date = models.DateField(
        verbose_name=("Start Date")
    )
    attention_date = models.DateField(
        verbose_name=("Attention Date")
    )
    appointment_type = models.CharField(
        max_length=2,
        choices=_APPOINTMENT_STATE,
        default='P',
        verbose_name=('Appointment Type')
    )

    def __str__(self):
        return self.title
