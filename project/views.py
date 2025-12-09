#file: project/views.py
#author: Anna Ni (annani@bu.edu)
#description: Views for managing clothing items and outfits in the Django project.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import ClothingItem, Outfit, OutfitItem
from .forms import ClothingItemForm, OutfitForm, OutfitItemForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView


class HomeView(TemplateView):
    template_name = 'project/home.html'

# ClothingItem Views
class ClothingItemListView(LoginRequiredMixin, ListView):
    model = ClothingItem
    template_name = 'project/clothing_list.html'
    context_object_name = 'clothing_items'
    login_url = '/login/'  # Redirect to login if not authenticated
    
    def get_queryset(self):
        # Only show items belonging to the logged-in user
        return ClothingItem.objects.filter(user=self.request.user)

class ClothingItemDetailView(LoginRequiredMixin, DetailView):
    model = ClothingItem
    template_name = 'project/clothing_detail.html'
    context_object_name = 'item'
    login_url = '/login/'

class ClothingItemCreateView(LoginRequiredMixin, CreateView):
    model = ClothingItem
    form_class = ClothingItemForm
    template_name = 'project/clothing_form.html'
    login_url = '/login/'
    
    def form_valid(self, form):
        # Automatically set the user to the logged-in user
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        # Check if there's a 'next' parameter to redirect back
        next_url = self.request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return response
    
    def get_success_url(self):
        # Check if there's a 'next' parameter
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('clothing_list')

# ClothingItem Update and Delete Views
class ClothingItemUpdateView(LoginRequiredMixin, UpdateView):
    model = ClothingItem
    form_class = ClothingItemForm
    template_name = 'project/clothing_form.html'
    success_url = reverse_lazy('clothing_list')
    login_url = '/login/'

class ClothingItemDeleteView(LoginRequiredMixin, DeleteView):
    model = ClothingItem
    template_name = 'project/clothing_confirm_delete.html'
    success_url = reverse_lazy('clothing_list')
    login_url = '/login/'

# Outfit Views
class OutfitListView(LoginRequiredMixin, ListView):
    model = Outfit
    template_name = 'project/outfit_list.html'
    context_object_name = 'outfits'
    login_url = '/login/'
    
    def get_queryset(self):
        return Outfit.objects.filter(user=self.request.user)

class OutfitDetailView(LoginRequiredMixin, DetailView):
    model = Outfit
    template_name = 'project/outfit_detail.html'
    context_object_name = 'outfit'
    login_url = '/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfit_items'] = OutfitItem.objects.filter(outfit=self.object)
        return context

class OutfitCreateView(LoginRequiredMixin, CreateView):
    model = Outfit
    form_class = OutfitForm
    template_name = 'project/outfit_form.html'
    success_url = reverse_lazy('outfit_list')
    login_url = '/login/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OutfitUpdateView(LoginRequiredMixin, UpdateView):
    model = Outfit
    form_class = OutfitForm
    template_name = 'project/outfit_form.html'
    success_url = reverse_lazy('outfit_list')
    login_url = '/login/'

class OutfitDeleteView(LoginRequiredMixin, DeleteView):
    model = Outfit
    template_name = 'project/outfit_confirm_delete.html'
    success_url = reverse_lazy('outfit_list')
    login_url = '/login/'
    
class OutfitItemCreateView(LoginRequiredMixin, CreateView):
    model = OutfitItem
    form_class = OutfitItemForm
    template_name = 'project/outfititem_form.html'
    login_url = '/login/'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        outfit_id = self.kwargs['outfit_id']
        form.instance.outfit = get_object_or_404(Outfit, pk=outfit_id, user=self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('outfit_detail', kwargs={'pk': self.kwargs['outfit_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfit'] = get_object_or_404(Outfit, pk=self.kwargs['outfit_id'])
        return context

class OutfitItemDeleteView(LoginRequiredMixin, DeleteView):
    model = OutfitItem
    template_name = 'project/outfititem_confirm_delete.html'
    login_url = '/login/'
    
    def get_success_url(self):
        return reverse_lazy('outfit_detail', kwargs={'pk': self.object.outfit.pk})
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'project/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Log the user in after registration
        login(self.request, self.object)
        return response