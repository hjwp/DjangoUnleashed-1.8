# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import migrations, models

POSTS = [
    {
        "title": "Django 1.0 Release",
        "slug": "django-10-released",
        "pub_date": date(2008, 9, 3),
        "startups": [],
        "tags": ["django", "python", "web"],
        "text": "THE Web Framework.",
    },
    {
        "title": "Simple Robots for Sale",
        "slug": "simple-robots-for-sale",
        "pub_date": date(2011, 2, 21),
        "startups": ["simple-robots"],
        "tags": ["augmented-reality", "python"],
        "text":
            "If only they would make "
            "spider bots.",
    },
    {
        "title": "Django Training",
        "slug": "django-training",
        "pub_date": date(2013, 1, 18),
        "startups": ["jambon-software"],
        "tags": ["django"],
        "text":
            "JamBon Software specializes in "
            "Django websites,and can train your "
            "engineers in the framework.",
    },
    {
        "title": "Django 1.8 Release",
        "slug": "django-18-released",
        "pub_date": date(2015, 4, 1),
        "startups": [],
        "tags": ["django", "python", "web"],
        "text": "No, it's not a joke!\n\n"
            "Lorem ipsum dolor sit amet,"
            "consectetur adipiscing elit, sed do"
            "eiusmod tempor incididunt ut labore"
            "et dolore magna aliqua. Ut enim ad"
            "minim veniam, quis nostrud"
            "exercitation ullamco laboris nisi ut"
            "aliquip ex ea commodo consequat."
            "Duis aute irure dolor in"
            "reprehenderit in voluptate velit"
            "esse cillum dolore eu fugiat nulla"
            "pariatur. Excepteur sint occaecat"
            "cupidatat non proident, sunt in"
            "culpa qui officia deserunt mollit"
            "anim id est laborum",
    },
    {
        "title": "More Django Info",
        "slug": "more-django-info",
        "pub_date": date(2015, 4, 8),
        "startups": ["jambon-software"],
        "tags": ["django", "web"],
        "text":
            "Remember that the official websites "
            "for Django and this book contain a "
            "number of extra resources.\n\n"
            "https://djangoproject.com\n"
            "https://django-unleashed.com\n\n"
            "Want more Django info? "
            "There's always my personal blog!\n\n"
            "https://AndrewsForge.com",
    },
    {
        "title": "New Django Version",
        "slug": "new-django-version",
        "pub_date": date(2020, 5, 15),
        "startups": [],
        "tags": ["django", "python", "web"],
        "text":
            "Better integration with "
            "HTML Boilerstrap 9.",
    },
]


def add_post_data(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Startup = apps.get_model(
        'organizer', 'Startup')
    Tag = apps.get_model('organizer', 'Tag')
    for post_dict in POSTS:
        post = Post.objects.create(
            title=post_dict['title'],
            slug=post_dict['slug'],
            text=post_dict['text'])
        post.pub_date = post_dict['pub_date']
        post.save()
        for tag_slug in post_dict['tags']:
            post.tags.add(
                Tag.objects.get(
                    slug=tag_slug))
        for startup_slug in post_dict['startups']:
            post.startups.add(
                Startup.objects.get(
                    slug=startup_slug))


def remove_post_data(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post_dict in POSTS:
        post = Post.objects.get(
            slug=post_dict['slug'])
        post.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('organizer', '0003_startup_data'),
    ]

    operations = [
        migrations.RunPython(
            add_post_data,
            remove_post_data)
    ]
