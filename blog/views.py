from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import (
    CreateView, ListView, View, YearArchiveView)

from .forms import PostForm
from .models import Post


class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post


class PostDelete(View):

    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug)
        return render(
            request,
            'blog/post_confirm_delete.html',
            {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')


def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug)
    return render(
        request,
        'blog/post_detail.html',
        {'post': post})


class PostList(ListView):
    model = Post


class PostUpdate(View):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form_update.html'

    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug)
        context = {
            'form': self.form_class(
                instance=post),
            'post': post,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug)
        bound_form = self.form_class(
            request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {
                'form': bound_form,
                'post': post,
            }
            return render(
                request,
                self.template_name,
                context)
