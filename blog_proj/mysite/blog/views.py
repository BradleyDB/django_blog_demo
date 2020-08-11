from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)


from .models import BlogPost,BlogComment
from .forms import BlogPostForm,BlogCommentForm


from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        #the __lte here means less than or equal to. It is a modifier you can use on your filters! Field Lookups. translates sql to python
        #the -published_date is published date with the newest to oldest
        return BlogPost.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = BlogPost

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_detail.html'
    form_class = BlogPostForm

    model = BlogPost

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_detail.html'
    form_class = BlogPostForm

    model = BlogPost

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost_list')

class DrafListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'blogpost_draft_list.html'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=True).order_by('created_date')


@login_required
def blogpost_publish(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    post.publish()
    return redirect('blogpost_detail',pk=pk)



##########COMMENT VIEWS##################


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)

    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogpost_detail',pk=post.pk)
    else:
        form = BlogCommentForm()
    return render(request,'blog/blogcomment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(BlogComment,pk=pk)
    comment.approve()
    return redirect('blogpost_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(BlogComment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blogpost_detail',pk=post_pk)
