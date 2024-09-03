from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.core.mail import send_mail
from django.views import View
from django.views.generic.edit import FormView

from .forms import AdditionalImageForm, CustomUserCreationForm, PersonalDetailsForm, EmployeeDetailsForm, EmployerDetailsForm, JobProfileForm, RelationshipGoalsForm
from .models import AdditionalImage, CustomUser, JobProfile,PersonalDetails
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

# class JobStatusView(TemplateView):
#     template_name='job_status.html'
    
# class JobDetailsView(TemplateView):
#     template_name='job_details.html'


# class ProfessionView(TemplateView):
#     template_name='profession.html'





class InterestView(TemplateView):
    template_name='interested.html'
    


def TestView(request):
    return render(request, 'index.html')

class SignupView(FormView):
    template_name = 'signup.html'  # Replace with your template path
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:personal_details')# Redirect to the homepage after successful signup

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        

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


    
class PersonalDetailsCreateView(LoginRequiredMixin, FormView):
    model = PersonalDetails
    form_class = PersonalDetailsForm
    template_name = 'personal_details.html'
    success_url = reverse_lazy('accounts:job_status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['additional_image_form'] = AdditionalImageForm(self.request.POST, self.request.FILES)
        else:
            context['additional_image_form'] = AdditionalImageForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        additional_image_form = context['additional_image_form']

        if form.is_valid() and additional_image_form.is_valid():
            # Assign the current user to the form instance
            personal_details = form.save(commit=False)
            personal_details.user = self.request.user
            personal_details.save()

            # Handle multiple additional images
            for image in self.request.FILES.getlist('image'):
                AdditionalImage.objects.create(user=self.request.user, image=image)

            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class JobStatusView(FormView):
    template_name = 'job_status.html'  # The template you provided
    form_class = JobProfileForm
    success_url = reverse_lazy('accounts:job_Details')  # Default success URL

    def form_valid(self, form):
        # Save the form data to the JobProfile model
        job_profile = form.save(commit=False)
        job_profile.user = self.request.user
        job_profile.save()

        # Check the selected job status
        selected_status = form.cleaned_data.get('job_status')

        # Debugging: Print the selected status
        print(f"Selected Status: {selected_status}")

        # Redirect based on the selected status
        if selected_status == 'employer':
            return redirect(reverse('accounts:job_Details', kwargs={'user_id': self.request.user.id}))
        elif selected_status == 'employee':
            return redirect(reverse('accounts:profession', kwargs={'user_id': self.request.user.id}))
        else:
            return redirect(reverse('accounts:relationship_goal', kwargs={'user_id': self.request.user.id}))
        
        # Use the default success_url if no redirection conditions are met
        return super().form_valid(form)

    
class EmployerDetailsView(UpdateView,LoginRequiredMixin):
    model = JobProfile
    form_class = EmployerDetailsForm
    template_name = 'job_details.html'  # Update this with the correct template path
     # Update with the correct URL name

    def get_object(self, queryset=None):
        # Assuming each user has only one job profile
        return JobProfile.objects.get(user=self.request.user)
    def get_success_url(self):
        # Pass the user_id into the URL
        return reverse_lazy('accounts:relationship_goal', kwargs={'user_id': self.request.user.id})
    
class EmployeeDetailsView(UpdateView,LoginRequiredMixin):
    model = JobProfile
    form_class = EmployeeDetailsForm
    template_name = 'profession.html'  # Update this with the correct template path
     # Update with the correct URL name

    def get_object(self, queryset=None):
        # Assuming each user has only one job profile
        return JobProfile.objects.get(user=self.request.user)
    def get_success_url(self):
        # Pass the user_id into the URL
        return reverse_lazy('accounts:relationship_goal', kwargs={'pk': self.request.user.id})
    
    
class RelationshipGoalsView(LoginRequiredMixin, UpdateView):
    model = PersonalDetails
    form_class = RelationshipGoalsForm
    template_name = 'relationship_goal.html'  # Update this with the correct template path
    success_url=reverse_lazy('accounts:interest')

    def get_object(self, queryset=None):
        # Assuming each user has only one job profile
        return PersonalDetails.objects.get(user=self.request.user)
    