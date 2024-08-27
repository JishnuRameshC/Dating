from django.forms import ValidationError
from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.mail import send_mail
from django.views import View
from django.http import JsonResponse
import random
from .models import CustomUser,OTP
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model,logout,authenticate, login
from django.contrib import messages

 

# Create your views here.

class FirstView(TemplateView):
    template_name='account/first.html'
    
# G1 accounts


# class LoginView(TemplateView):
#     template_name='login.html'
    
class PersonalDetailsView(TemplateView):
    template_name='personal_details.html'

class JobStatusView(TemplateView):
    template_name='account/job_status.html'
    
class JobDetailsView(TemplateView):
    template_name='account/job_details.html'


class ProfessionView(TemplateView):
    template_name='account/profession.html'


class Rel_GoalView(TemplateView):
    template_name='account/relationship_goal.html'


class InterestView(TemplateView):
    template_name='account/interested.html'
    


def TestView(request):
    return render(request, 'index.html')

class GenerateOTPView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        # Delete existing OTP records
        OTP.objects.filter(email=email, mobile=mobile).delete()

        # Generate and send new OTP
        otp = str(random.randint(100000, 999999))
        otp_record = OTP.objects.create(email=email, mobile=mobile, otp=otp)

        # Send OTP via email
        try:
            send_mail(
                'Your OTP Code',
                f'Your OTP is {otp}',
                'from@example.com',  # Change this to your sender email
                [email],
                fail_silently=False,
            )
            return JsonResponse({'status': 'ok', 'message': 'OTP sent to your email.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('name')
        otp_input = request.POST.get('otp')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the mobile number already exists
        if CustomUser.objects.filter(mobile=mobile).exists():
            return JsonResponse({'status': 'error', 'message': 'A user with this mobile number already exists.'}, status=400)

        # Check if passwords match
        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match.'}, status=400)

        try:
            # Validate OTP
            otp_record = OTP.objects.get(email=email, mobile=mobile, otp=otp_input)
            if not otp_record.is_valid():
                return JsonResponse({'status': 'error', 'message': 'Invalid or expired OTP.'}, status=400)

            # Create user
            User = get_user_model()
            user = User(username=username, email=email, mobile=mobile)
            user.set_password(password)
            user.is_active = True
            user.save()

            # Mark OTP as verified
            otp_record.is_verified = True
            otp_record.save()

            # Authenticate the user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:personal_details')
            
            


            return JsonResponse({'status': 'error', 'message': 'Registration successful, but failed to log in.'}, status=400)

        except OTP.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid OTP, email, or mobile.'}, status=400)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        # Render the login form
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'status': 'error', 'message': 'Username and password are required.'}, status=400)

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'}, status=400)

        # Login user
        login(request, user)

        return JsonResponse({'status': 'ok', 'message': 'Login successful.'})
    
def signout(request):
    logout(request)
    return redirect('accounts:login')