from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path('pay-now/', pay_now, name='pay_now'),
    path('process-payment/', process_payment, name='process_payment'),
    path('services/web-development/', web_development, name='web_development'),
    path('services/seo-optimization/', seo_optimization, name='seo_optimization'),
    path('services/digital-marketing/', digital_marketing, name='digital_marketing'),
    path("blog/future-of-ai-powered-web-development-2026/",blog1,name="blog1"),
    path("blog/why-every-small-business-needs-seo-optimized-website/",blog2,name="blog2"),
    path("blog/how-technical-seo-can-double-your-website-traffic/",blog3,name="blog3"),
    path("blog/custom-software-vs-off-the-shelf-software/",blog4,name="blog4"),
    path("blog/django-vs-wordpress-which-is-best-for-business/",blog5,name="blog5"),
    path("blog/django-vs-wordpress-which-platform-is-best-for-growing-businesses/",blog6,name="blog6"),
]