#File: views.py
#Author: Anna Ni (annani@bu.edu)
#Description: Implements views for displaying lists of profiles and details for individual profiles in the Mini Insta application.


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm
from django.urls import reverse





class ProfileListView(ListView):
    #Display a list of all Profile objects.
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    # Display detailed information for a single Profile object.
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

class PostDetailView(DetailView):
    # Display detailed information for a single Post object.
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs["pk"])
        context["profile"] = profile
        return context

    def form_valid(self, form):
        # attach Post to Profile
        profile = Profile.objects.get(pk=self.kwargs["pk"])
        form.instance.profile = profile

        # save the Post first
        self.object = form.save()

        # handle uploaded files (if any)
        files = self.request.FILES.getlist('files')
        for f in files:
            Photo.objects.create(post=self.object, image_file=f)

        return super().form_valid(form)

    def get_success_url(self):
        # after post is created, show the post detail
        return reverse("mini_insta:show_post", args=[self.object.pk])


class UpdateProfileView(UpdateView):
    # Allow users to update an existing Profile.  
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    
class DeletePostView(DeleteView):
    # Allow users to delete an existing Post.
    model = Post
    template_name = 'mini_insta/delete_post_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = post
        context['profile'] = post.profile
        return context

    def get_success_url(self):
        post = self.get_object()
        return reverse('mini_insta:show_profile', kwargs={'pk': post.profile.pk})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['caption', 'image_url']  # editable fields
    template_name = 'mini_insta/update_post_form.html'  # template you'll create

    def get_success_url(self):
        # After saving, go back to the updated post’s detail page
        return reverse_lazy('mini_insta:show_post', kwargs={'pk': self.object.pk})