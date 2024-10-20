from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="index"),
  path('about', views.about, name="about"),
  path('services', views.service, name="services"),
  path('service_details/<int:service_id>', views.service_details, name='service_details'),
  path('teams', views.team, name="team"),
  
  path("blog", views.blog_index, name="blog"),
  path("blog_details/<int:blog_id>", views.blog_details, name="blog_details"),
  path("blog_details/<int:blog_id>/comment", views.blog_comment, name="blog_comment"),
  
  path("subscribed", views.newsletter_subscribe, name="subscribe"),
  
  path('appointment', views.book_appointment, name="appointment"),
  path('appointment/success/<int:appointment_id>/', views.appointment_success, name='appointment_success'),
  path('appointment/failure/', views.appointment_failure, name='appointment_failure'),
  
  path('contact', views.contact_form, name="contacts"),
  path('contact/success/', views.contact_success, name='contact_success'),
  path('contact/failure/', views.contact_failure, name='contact_failure'),
]