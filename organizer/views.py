from django.shortcuts import (
    get_object_or_404, redirect, render)

from .forms import TagForm
from .models import Startup, Tag


def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup})


def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()})


def tag_create(request):
    # If the form has been submitted...
    if request.method == 'POST':
        # Bind the form to the POST data
        form = TagForm(request.POST)
        # If validation rules pass
        if form.is_valid():
            # Create new tag object
            new_tag = form.save()
            # Redirect to new Tag
            # uses Tag.get_absolute_url
            return redirect(new_tag)
        # implicit else:
        #   bound form (with errors)
        #   passed back to template (line 45)
    # if request.method != POST
    else:
        # create an unbound form instance
        form = TagForm()
    # return either:
    #     (1) the bound+invalid form on line 27
    #     (2) the unbound form from line 41
    return render(
        request,
        'organizer/tag_form.html',
        {'form': form})


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})
