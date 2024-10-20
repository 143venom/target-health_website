from django.db import models
from datetime import datetime
# Create your models here.


# Model to represent a slider on the homepage or similar areas

class Slider(models.Model): 
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    buttontext =  models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider', default="slider/banner.png")


    def __str__(self):
        return self.title
    

# Model for features that might be highlighted on service page

class Feature(models.Model):
    icon = models.CharField(max_length=200, default="flaticon-electrocardiogram")  # thirdparty icon
    title = models.CharField(max_length=255)
    description = models.TextField()
    buttontext = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Model for different qualities for About Section

class Quality(models.Model):
  title = models.CharField(max_length=120)

  def __str__(self):
    return self.title
  

# Model for "About Us" section

class About(models.Model):
  title =  models.CharField(max_length=200)
  maintitle =  models.CharField(max_length=200)
  description =  models.TextField()
  image1 = models.ImageField(upload_to='about', default="about/default.jpg")
  image2 = models.ImageField(upload_to='about', default="about/defaultt.jpg")
  features = models.ManyToManyField(Quality, related_name='qualities')

  def __str__(self):
    return self.title


# Model for team members, such as doctors 

class DoctorTeam(models.Model):
  name = models.CharField(max_length=200)
  designation = models.CharField(max_length=200)
  image = models.ImageField(upload_to='doctor', default="doctor/default.jpg")
  
  def __str__(self):
      return self.name


# Model for different services offered

class OurServiceContent(models.Model):
   title = models.CharField(max_length=120)
   description = models.TextField()

   def __str__(self):
       return self.title


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True)    # Optional category field

    def __str__(self):
        return self.name   

class Service(models.Model):
  title = models.CharField(max_length=120)
  introduction = models.TextField()
  equipments = models.ManyToManyField(Equipment, related_name='equipments')
  conclusion = models.TextField()
  image = models.ImageField(upload_to='service', default="service/default.jpg")

  def __str__(self):
      return self.title
  

# Model for business-related information tabs

class BusinessInfo(models.Model):
    title = models.CharField(max_length=255)
    maintitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service', default="service/defaultea.jpg")

    
    def __str__(self):
        return self.title


# Model for client testimonials

class Testimonial(models.Model):
  client_name = models.CharField(max_length=120)
  description = models.TextField()
  backgroundimage = models.ImageField(upload_to='testimonial', default="testimonial/default.jpg")
  
  def __str__(self):
      return self.client_name
  

# Model for Emergency Services like Make an Appointment, etc.

class EmergencyService(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  buttontext = models.CharField(max_length=200)
  background_image = models.ImageField(upload_to='emergency_bg', default="emergency_bg/default.png")
  

  def __str__(self):
      return self.title
  

# Model for site-wide content such as logos, contact information, and footer content

class SiteContent(models.Model):
   logo = models.ImageField(upload_to='logos/', default="logos/Logo.png")
   header_email = models.EmailField()
   header_phone = models.CharField(max_length=20)
   footer_content = models.TextField()
   linkedin_link = models.URLField(blank=True, null=True)
   google_link = models.URLField(blank=True, null=True)
   facebook_link = models.URLField(blank=True, null=True)
   company_address = models.CharField(max_length=150)

   def __str__(self):
      return 'Site Settings'
   

# Model for blog posts  

class Blog(models.Model):
  author = models.CharField(max_length=200)
  author_image = models.ImageField(default="blog/profile/default.jpg", upload_to='blog/profile')
  title = models.CharField(max_length=200)
  blog_desc = models.TextField()
  image = models.ImageField(default="blog/post/default.jpg", upload_to='blog/post')
  created_on = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title
  

# Model for comments on blog posts

class Comment(models.Model):
  posted_by = models.CharField(max_length=100, blank=False)
  commenter_email = models.EmailField(blank=False)
  commenter_website = models.CharField(max_length=100, blank=False)
  comment_desc = models.CharField(max_length=300, blank=False)
  commenter_image = models.ImageField(default="blog/profile/default.jpg", upload_to='blog/profile')
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
  created_on = models.DateTimeField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.posted_by
  

# Model for Subscription on blog page

class Subscription(models.Model):
  email = models.EmailField()
  subscribed_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email
  

# Model for different departments

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# Model for appointment scheduling

class Appointment(models.Model):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorTeam, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.appointment_date} at {self.appointment_time} with {self.doctor}"
    

class BradcamImage(models.Model):
   about_bg = models.ImageField(upload_to='bradcam_img', default="bradcam_img/banner.png")
   service_bg = models.ImageField(upload_to='bradcam_img', default="bradcam_img/banner.png")
   blog_bg = models.ImageField(upload_to='bradcam_img', default="bradcam_img/banner.png")
   team_bg = models.ImageField(upload_to='bradcam_img', default="bradcam_img/banner.png")
   contact_bg = models.ImageField(upload_to='bradcam_img', default="bradcam_img/banner.png")

   def __str__(self):
       return "BradCam BG Image"
   
    

  