from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Tag, PostView
from .forms import PostForm, CommentForm
from django.http import JsonResponse

@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    PostView.objects.create(post=post, viewed_by=request.user)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_update.html'
    success_url = reverse_lazy('posts:post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:post_list')

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_update.html'

    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={'pk': self.object.post.pk})
