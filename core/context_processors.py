from .models import EmergencyService, SiteContent, Department, DoctorTeam, BradcamImage

def get_emergency_service(request):
  return {
    'emergency_service': EmergencyService.objects.all(),
    }


def get_site_content(request):
  return {
    'site_content': SiteContent.objects.first(),
    'bradcam_bg': BradcamImage.objects.first(),
    }


def global_context(request):
    return {
        'departments': Department.objects.all(),
        'doctors': DoctorTeam.objects.all(),
    }