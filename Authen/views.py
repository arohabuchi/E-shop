from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from Authen.forms import CustomerRegistrationForm

# Create your views here.
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Authen/CustomerRegistration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #send mail or message
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'Authen/CustomerRegistration.html', locals())