from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.db.models import Count

from .forms import *
from .models import *

# Create your views here.

def get_context(*args):
  context = {}
  if 'about' in args:
    context['about'] = About.objects.first()
  if 'doctors' in args:
    context['doctors'] = DoctorTeam.objects.all()
  if 'services' in args:
    context['services'] = Service.objects.all()
  if 'testimonials' in args:
    context['testimonials'] = Testimonial.objects.all()
  if 'features' in args:
    context['features'] = Feature.objects.all()
  if 'our_service' in args:
    context['our_service'] = OurServiceContent.objects.first()
  if 'business_info' in args:
    context['business_info'] = BusinessInfo.objects.all()
  if 'sliders' in args:
    context['sliders'] = Slider.objects.all()
  if 'blogs' in args:
    context['blogs'] = Blog.objects.order_by('-created_on')
  return context

def home(request):
    context = get_context(
    'sliders', 'about', 'our_services', 'services', 'testimonials', 'features', 'business_info', 'blogs'
    )
    return render(request, "index.html", context)


def about(request):
   context = get_context(
    'about', 'testimonials', 'business_info', 'blogs', 'doctors'
    )
   return render(request, "about.html", context)
   


def team(request):
    context = get_context(
    'testimonials', 'business_info', 'doctors'
    )
    return render(request, "teams.html", context)


def service(request):
    context = get_context(
    'features', 'testimonials', 'business_info', 'blogs', 'our_service', 'services'
    )
    return render(request, "services.html", context)

def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    # Split the equipment into two lists
    equipment_list = list(service.equipments.all())
    mid_index = len(equipment_list) // 2
    first_column = equipment_list[:mid_index]
    second_column = equipment_list[mid_index:]
    return render(request, 'service_details.html', {
        'service': service,
        'first_column': first_column,
        'second_column': second_column,
    })


# Contact View

def contact_form(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      subject = form.cleaned_data["subject"]
      message = form.cleaned_data["message"]

      html_content = render_to_string(
                "emails/formdisplay.html",
                {
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message,
                },
            )

      send_mail("You got a mail!!!", message, email, ['info@targethealthuae.com'], html_message=html_content, fail_silently=False)
    
      return redirect("contact_success")
    return redirect("contact_failure")
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})

def contact_success(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'success_failure_pages/con_success.html', {'appointment': appointment})

def contact_failure(request):
    return render(request, 'success_failure_pages/con_failure.html')



# Blog and Comment View

items_per_page = 5

def blog_index(request):
  blog_list = Blog.objects.annotate(num_comments=Count('comment')).order_by('-created_on')
  paginator = Paginator(blog_list, items_per_page)
  page_number = request.GET.get("page")
  blogs = paginator.get_page(page_number)
  context = {'blogs': blogs}
  return render(request, 'blog.html', context)



def blog_details(request, blog_id):
  blog = Blog.objects.get(pk=blog_id)
  paragraphs = blog.blog_desc.split('\n')
  blogs = Blog.objects.all().order_by('-created_on')

  current_index = list(blogs).index(blog)
  if current_index > 0:
    previous_post = blogs[current_index - 1]
  else:
    previous_post = None

  if current_index < len(blogs) - 1:
    next_post = blogs[current_index + 1]
  else:
    next_post = None

  comments = Comment.objects.all().filter(blog_id=blog_id).order_by('-created_on')
  context = {'blog': blog, 'comments': comments, 'blogs': blogs, 'previous_post': previous_post, 
             'next_post': next_post, 'paragraphs': paragraphs, 'current_blog': blog,}
  return render(request, 'blogdetails.html', context)



def blog_comment(request, blog_id):
  if request.method == "POST":
    posted_by = request.POST["name"]
    comment_desc = request.POST["comment"]
    commenter_email = request.POST["email"]
    commenter_website = request.POST["website"]
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = Comment(posted_by=posted_by, comment_desc=comment_desc, commenter_email=commenter_email, 
                      commenter_website=commenter_website, blog=blog)
    comment.save()
    
  return redirect(request.META.get('HTTP_REFERER', '/'))


# Appointment View

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            subject = 'Appointment Confirmation'
            message = f'Your appointment has been successfully booked.\n\nDetails:\nName: {appointment.name}\nDate: {appointment.appointment_date}\nTime: {appointment.appointment_time}\nDepartment: {appointment.department}\nDoctor: {appointment.doctor}'
            recipient_list = [appointment.email]
            send_mail(subject, message, 'info@targethealthuae.com', recipient_list)

            return redirect('appointment_success', appointment_id=appointment.id)
        return redirect('appointment_failure')
    else:
        form = AppointmentForm()
    return render(request, 'base.html', {'form': form})


def appointment_success(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'success_failure_pages/success.html', {'appointment': appointment})

def appointment_failure(request):
    return render(request, 'success_failure_pages/failure.html')



# Subscription View

def newsletter_subscribe(request):
  if request.method == "POST":
      email = request.POST.get("email", "").strip()
      
      if email:
        if Subscription.objects.filter(email=email).exists():
          html_response = '''
          <html>
          <body style="text-align: center;">
              <p>Email is already taken. Please choose another email.</p>
              <a href="javascript:history.back()">Go Back</a>
          </body>
          </html>
          '''
          return HttpResponse(html_response, status=400)
        
        else:
          Subscription.objects.create(email=email)
          return redirect("blog")
      else:
        return HttpResponse("Email field is required", status=400)
  return HttpResponse("Invalid request", status=400)



