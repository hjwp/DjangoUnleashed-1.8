from django.shortcuts import (
    get_object_or_404, render)
from django.views.generic import View

from .models import Post


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


class PostList(View):
    template = 'blog/post_list.html'

    def get(self, request):
        return render(
            request,
            self.template,
            {'post_list': Post.objects.all()})
