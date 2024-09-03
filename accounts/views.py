from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.mail import send_mail
from django.views import View
from django.views.generic.edit import FormView

from .forms import AdditionalImageForm, CustomUserCreationForm, CustomUserForm
from .models import AdditionalImage, CustomUser
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView
from django.contrib.auth import get_user_model,logout,authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

 

# Create your views here.

class FirstView(TemplateView):
    template_name='first.html'
    
# G1 accounts


# class LoginView(TemplateView):
#     template_name='login.html'
    
# class PersonalDetailsView(TemplateView):
#     template_name='personal_details.html'

class JobStatusView(TemplateView):
    template_name='job_status.html'
    
class JobDetailsView(TemplateView):
    template_name='job_details.html'


class ProfessionView(TemplateView):
    template_name='profession.html'


class Rel_GoalView(TemplateView):
    template_name='relationship_goal.html'


class InterestView(TemplateView):
    template_name='interested.html'
    


def TestView(request):
    return render(request, 'index.html')

class SignupView(FormView):
    template_name = 'signup.html'  # Replace with your template path
    form_class = CustomUserCreationForm
    success_url = None # Redirect to the homepage after successful signup

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.success_url = reverse_lazy('accounts:personal_details', kwargs={'pk': user.pk})

        return super().form_valid(form)
    
    def form_invalid(self, form):
        # You can handle what happens when the form is invalid
        return super().form_invalid(form)
    



class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username_or_mobile = request.POST.get('username')
        password = request.POST.get('password')
        context = {
            'username': username_or_mobile,  # Pass the input back to the template in case of error
        }

        if not username_or_mobile or not password:
            context['error_message'] = 'Email/Mobile and password are required.'
            return render(request, 'login.html', context)

        # Try to find the user based on email or mobile
        user_obj = None
        try:
            user_obj = CustomUser.objects.get(email=username_or_mobile)
        except CustomUser.DoesNotExist:
            try:
                user_obj = CustomUser.objects.get(mobile=username_or_mobile)
            except CustomUser.DoesNotExist:
                user_obj = None

        if user_obj is None:
            context['error_message'] = 'Invalid email/mobile or password.'
            return render(request, 'login.html', context)
        
        # Authenticate user
        user = authenticate(request, username=user_obj.email, password=password)
        if user is None:
            context['error_message'] = 'Invalid email/mobile or password.'
            return render(request, 'login.html', context)

        # Login user
        login(request, user)
        return redirect('Dating:home')
    
def signout(request):
    logout(request)
    return redirect('accounts:login')


    
class PersonalDetailsCreateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'personal_details.html'
    success_url = reverse_lazy('Dating:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['additional_image_form'] = AdditionalImageForm(self.request.POST, self.request.FILES)
        else:
            context['additional_image_form'] = AdditionalImageForm()
        context['additional_images'] = self.object.additional_images.all()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        additional_image_form = context['additional_image_form']

        if additional_image_form.is_valid():
            self.object = form.save()

            # Handle multiple additional images
            for image in self.request.FILES.getlist('image'):
                AdditionalImage.objects.create(user=self.object, image=image)

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
