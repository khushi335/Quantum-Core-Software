from django.shortcuts import render, redirect
from django.conf import settings
import urllib.parse

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def contact(request):
    return render(request,"main/contact.html")

def pay_now(request):
    return render(request, 'main/pay_now.html')

def process_payment(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        reason = request.POST.get('reason')
        
        # PayPal Base URL (Use Sandbox from your config if testing)
        paypal_url = settings.PAYPAL_URL 
        
        # Build the PayPal Query Parameters
        params = {
            'cmd': '_xclick',
            'business': settings.PAYPAL_PERSONAL_EMAIL,
            'item_name': reason,
            'amount': amount,
            'currency_code': 'USD',
            'return': request.build_absolute_uri('/payment-success/'),
            'cancel_return': request.build_absolute_uri('/pay-now/'),
        }
        
        # Redirect directly to PayPal
        query_string = urllib.parse.urlencode(params)
        return redirect(f"{paypal_url}?{query_string}")
    
    return redirect('pay_now')

def web_development(request):
    return render(request, 'main/web_development.html')

def seo_optimization(request):
    return render(request, 'main/seo_optimization.html')

def digital_marketing(request):
    return render(request, 'main/digital_marketing.html')