from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("conatct/",contact,name="contact"),\
    path('pay-now/', pay_now, name='pay_now'),
    path('process-payment/', process_payment, name='process_payment'),
    path('services/web-development/', web_development, name='web_development'),
    path('services/seo-optimization/', seo_optimization, name='seo_optimization'),
    path('services/digital-marketing/', digital_marketing, name='digital_marketing'),
]