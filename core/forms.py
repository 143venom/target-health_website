from django import forms

from .models import *

class ContactForm(forms.Form):
  name = forms.CharField(max_length=255)
  email = forms.EmailField()
  subject = forms.CharField()
  message = forms.CharField(widget=forms.Textarea)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'department', 'doctor', 'name', 'phone_number', 'email']
        widgets = {
            'department': forms.Select(),
            'doctor': forms.Select(),
        }
