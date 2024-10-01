from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models
from .models import post_model,input_d
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from django.shortcuts import render
from .forms import post_form,input_form
from . import forms

class input_da(CreateView):
    model = models.input_d
    form_class = forms.input_form
    template_name = 'input.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# Create your views here.
# def post(request):
#     if request.method == 'POST':
#         form = post_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#     else:
#         form = post_form()
#     return render(request, 'post.html',{'form':form})

# add post using class based view
@method_decorator(login_required,name='dispatch')
class add_post_create_view(CreateView):
    model = models.post_model
    form_class = forms.post_form
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



# def edit_post(request,id):
#     post = models.post_model.objects.get(pk=id)
#     form = forms.post_form(instance=post)
#     if request.method == 'POST':
#         form = post_form(request.POST, request.FILES,instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     return render(request, 'post.html',{'form':form})

@method_decorator(login_required,name='dispatch')
class update_view(UpdateView):
    model = models.post_model
    form_class = forms.post_form
    template_name = 'post.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

@method_decorator(login_required,name='dispatch')
class delete_view(DeleteView):
    model = models.post_model
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    
# def delete_post(request,id):
#     post = models.post_model.objects.get(pk=id)
#     post.delete()
#     return redirect('home')
