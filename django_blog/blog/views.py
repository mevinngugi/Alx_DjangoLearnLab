# This import is starting to look ugly. Update to import all
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            # We login the user after a successful registration
            login(request, user)
            return redirect('home')
        
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/profile.html', context)


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all comments that have a relation to the current post
        context['comments'] = Comment.objects.filter(post=self.object.id)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('posts')

    # Ensure that we bind the logged in user id to post.author
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    success_url = reverse_lazy('posts')
    # Overriding the template because by default it was picking the post create form
    template_name = 'blog/post_form_update.html'

    def test_func(self):
        post = self.get_object()
        # Only allow super user and the owner of the post to edit post
        if self.request.user.is_superuser:
            return True
        elif self.request.user.id == post.author_id:
            return True


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        # Only allow super user and the owner of the post to delete post
        if self.request.user.is_superuser:
            return True
        elif self.request.user.id == post.author_id:
            return True


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pk as set in the urls
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Make the post object accessible in the html form
        context['post'] = post
        # Get all the comment related to the post
        context['comments'] = Comment.objects.filter(post=post)
        return context

    def form_valid(self, form):
        # Get the current post if not 404
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)
        # Connect the comment to the post 
        form.instance.post = post
        # Connect the comment to the logged in author
        form.instance.author = self.request.user
        messages.success(self.request, 'Comment saved successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    # Leaving out the template name for now to see if it will pick the create comment template instead of update
    template_name = 'blog/comment_update_form.html'

    def test_func(self):
        comment = self.get_object()
        # Only allow super user and the owner of the comment to edit comment
        if self.request.user.is_superuser:
            return True
        elif self.request.user.id == comment.author_id:
            return True

    def get_success_url(self):
        comment = self.get_object()
        post_id = comment.post.id
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        # Only allow super user and the owner of the comment to edit comment
        if self.request.user.is_superuser:
            return True
        elif self.request.user.id == comment.author_id:
            return True

    def get_success_url(self):
        comment = self.get_object()
        post_id = comment.post.id
        return reverse_lazy('post_detail', kwargs={'pk': post_id})