#File: views.py
#Author: Anna Ni (annani@bu.edu)
#Description: Implements views for displaying lists of profiles and details for individual profiles in the Mini Insta application.


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login  
from django.urls import reverse
from .models import Profile, Post, Photo, Like, Follow
from .forms import CreatePostForm, UpdateProfileForm, CreateProfileForm  
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add the logged-in user's profile to context (if authenticated)
        if self.request.user.is_authenticated:
            # Use .first() to get the first profile if multiple exist
            context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        else:
            context['user_profile'] = None
            
        return context

class PostDetailView(DetailView):
    # Display detailed information for a single Post object.
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(LoginRequiredMixin, CreateView):
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


class CreateProfileView(CreateView):
    """View to create a new Profile along with a User account."""
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_insta/create_profile_form.html'
    
    def get_context_data(self, **kwargs):
        """Add UserCreationForm to the context."""
        context = super().get_context_data(**kwargs)
        
        # Add the UserCreationForm to context
        if 'user_creation_form' not in context:
            context['user_creation_form'] = UserCreationForm()
        
        return context
    
    def form_valid(self, form):
        """
        Handle the form submission.
        Create the User account first, then attach it to the Profile.
        """
        # Reconstruct the UserCreationForm from POST data
        user_creation_form = UserCreationForm(self.request.POST)
        
        # Validate the UserCreationForm
        if user_creation_form.is_valid():
            # Save the User object
            user = user_creation_form.save()
            
            # Log the user in
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            # Attach the User to the Profile instance
            form.instance.user = user
            
            # Delegate saving the Profile to the superclass
            return super().form_valid(form)
        else:
            # If UserCreationForm is invalid, re-render with errors
            context = self.get_context_data(form=form)
            context['user_creation_form'] = user_creation_form
            return self.render_to_response(context)
    
    def get_success_url(self):
        """Redirect to the newly created profile page."""
        return reverse('mini_insta:show_profile', kwargs={'pk': self.object.pk})


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    # Allow users to update an existing Profile.  
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    
class DeletePostView(LoginRequiredMixin, DeleteView):
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


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['caption']  # Only caption can be updated
    template_name = 'mini_insta/update_post_form.html'

    def get_success_url(self):
        # After saving, go back to the updated post's detail page
        return reverse('mini_insta:show_post', kwargs={'pk': self.object.pk})
    
class ShowFollowersDetailView(DetailView):
    #Display all followers of a Profile.
    model = Profile
    template_name = 'mini_insta/show_followers.html'
    context_object_name = 'profile'


class ShowFollowingDetailView(DetailView):
    #Display all profiles that this Profile is following.
    model = Profile
    template_name = 'mini_insta/show_following.html'
    context_object_name = 'profile'
    
class PostFeedListView(LoginRequiredMixin, ListView):
    #Display the post feed for a given Profile.
    model = Post
    template_name = 'mini_insta/show_feed.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        #Get the posts for the feed of the profile specified by pk.
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return profile.get_post_feed()
    
    def get_context_data(self, **kwargs):
        #Add the profile to the context.
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        return context
    
class SearchView(LoginRequiredMixin, ListView):
    """Search for Profiles and Posts based on a query string."""
    template_name = 'mini_insta/search_results.html'
    context_object_name = 'posts'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Handle the request. If no query is present, show the search form.
        Otherwise, proceed with the ListView to show results.
        """
        # Check if 'query' is in the GET parameters
        if 'query' not in self.request.GET or not self.request.GET.get('query'):
            # No query yet - show the search form
            profile = Profile.objects.get(pk=self.kwargs['pk'])
            context = {'profile': profile}
            return render(request, 'mini_insta/search.html', context)
        
        # Query exists - continue with ListView
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        """
        Return Posts that match the search query.
        A post matches if the query is in its caption.
        """
        query = self.request.GET.get('query', '')
        
        # Search for posts where the query appears in the caption
        posts = Post.objects.filter(caption__icontains=query).order_by('-timestamp')
        
        return posts
    
    def get_context_data(self, **kwargs):
        #Add additional context data for the template.
       
        context = super().get_context_data(**kwargs)
        
        # Get the profile for whom we're searching
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        
        # Get the query string
        query = self.request.GET.get('query', '')
        context['query'] = query
        
        # Get posts matching the query (already in context as 'posts')
        context['posts'] = self.get_queryset()
        
        # Get profiles matching the query
        # Match if query is in username, display_name, or bio_text
        profiles = Profile.objects.filter(
            Q(username__icontains=query) |
            Q(display_name__icontains=query) |
            Q(bio_text__icontains=query)
        )
        context['profiles'] = profiles
        
        return context

class FollowProfileView(LoginRequiredMixin, TemplateView):
    """Allow a logged-in user to follow another profile."""
    
    def dispatch(self, request, *args, **kwargs):
        # Get the profile to follow (the "other" profile)
        profile_to_follow = get_object_or_404(Profile, pk=self.kwargs['pk'])
        
        # Get the logged-in user's profile
        logged_in_profile = Profile.objects.get(user=self.request.user)
        
        # Don't allow a profile to follow itself
        if logged_in_profile != profile_to_follow:
            # Create a Follow object if it doesn't already exist
            Follow.objects.get_or_create(
                follower_profile=logged_in_profile,
                profile=profile_to_follow
            )
        
        # Redirect back to the profile page
        return redirect('mini_insta:show_profile', pk=profile_to_follow.pk)


class UnfollowProfileView(LoginRequiredMixin, TemplateView):
    """Allow a logged-in user to unfollow another profile."""
    
    def dispatch(self, request, *args, **kwargs):
        # Get the profile to unfollow
        profile_to_unfollow = get_object_or_404(Profile, pk=self.kwargs['pk'])
        
        # Get the logged-in user's profile
        logged_in_profile = Profile.objects.get(user=self.request.user)
        
        # Delete the Follow object if it exists
        Follow.objects.filter(
            follower_profile=logged_in_profile,
            profile=profile_to_unfollow
        ).delete()
        
        # Redirect back to the profile page
        return redirect('mini_insta:show_profile', pk=profile_to_unfollow.pk)


class LikePostView(LoginRequiredMixin, TemplateView):
    """Allow a logged-in user to like a post."""
    
    def dispatch(self, request, *args, **kwargs):
        # Get the post to like
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        
        # Get the logged-in user's profile
        logged_in_profile = Profile.objects.get(user=self.request.user)
        
        # Don't allow a profile to like their own post
        if logged_in_profile != post.profile:
            # Create a Like object if it doesn't already exist
            Like.objects.get_or_create(
                profile=logged_in_profile,
                post=post
            )
        
        # Redirect back to the post detail page
        return redirect('mini_insta:show_post', pk=post.pk)


class UnlikePostView(LoginRequiredMixin, TemplateView):
    """Allow a logged-in user to unlike a post."""
    
    def dispatch(self, request, *args, **kwargs):
        # Get the post to unlike
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        
        # Get the logged-in user's profile
        logged_in_profile = Profile.objects.get(user=self.request.user)
        
        # Delete the Like object if it exists
        Like.objects.filter(
            profile=logged_in_profile,
            post=post
        ).delete()
        
        # Redirect back to the post detail page
        return redirect('mini_insta:show_post', pk=post.pk)