from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import sign
from django.urls import reverse_lazy

class Login_view(LoginView):
    template_name = 'login_form.html'
    # success_url = reverse_lazy('home')
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Fail')
        return super().form_invalid(form)

# Create your views here.ZVXZ
def signup(request):
    if request.method == 'POST':
        form = sign(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Sign Up Successfully')
            print(form.cleaned_data)
            return redirect('login')
    else:
        form = sign()
    return render(request,'form.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            usernam = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username = usernam, password = upass)
            if user is not None:
                messages.success(request,'Logged In Successfully')
                login(request,user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'login_form.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('login')