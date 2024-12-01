from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import Doctor, Appointment, Patient
from .serializers import DoctorSerializer, AppointmentSerializer, PatientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from django.http import HttpResponse
from rest_framework.reverse import reverse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Clinic API</h1><p>Use the <a href='/api/'>API</a>.</p>")

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'doctors': reverse('doctor-list', request=request, format=format),
        'appointments': reverse('appointment-list', request=request, format=format),
        'patients': reverse('patient-list', request=request, format=format),
    })

class DoctorViewSet(viewsets.ModelViewSet):
    ...
    
    @permission_classes([IsAdminUser])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class AppointmentViewSet(viewsets.ModelViewSet):
    ...


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=True, methods=['get'])
    def timeslots(self, request, pk=None):
        doctor = self.get_object()
        return Response(doctor.available_times)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
