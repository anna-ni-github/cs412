#File: views.py
#Author: Anna Ni (annani@bu.edu)
#Description: Implements views for displaying lists of profiles and details for individual profiles in the Mini Insta application.


from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post
from .forms import CreatePostForm
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
        profile = Profile.objects.get(pk=self.kwargs["pk"])
        form.instance.profile = profile  # attach Post to Profile
        response = super().form_valid(form)

        # after saving Post, create Photo linked to it
        image_url = self.request.POST.get("image_url")
        if image_url:
            Photo.objects.create(post=self.object, image_url=image_url)

        return response

    def get_success_url(self):
        # after post is created, show the post detail
        return reverse("mini_insta:show_post", args=[self.object.pk])
    