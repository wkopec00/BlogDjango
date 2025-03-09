from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

all_posts = [
    {
        'slug':'motorowka-na-mazurach',
        'image':'motorowka.jpg',
        'autor':'Wojtek',
        'date': date(2024, 10, 10),
        'title':'Motorówka na mazurach',
        'excerpt':'Pływanie motorówką po jeziorach mazurskich...',
        'content':"""
                {% lorem 7 b random %}
                {% lorem 1 b random %}
        """
    },
    {
        'slug':'programowanie-jest-super',
        'image':'coding.jpg',
        'autor':'Wojtek',
        'date': date(2024, 12, 15),
        'title':'Python jest super',
        'excerpt':'Programowanie w języku Python jest bardzo proste...',
        'content':"""
                {% lorem 2 b random %}
                {% lorem 5 b random %}
        """
    },
    {
        'slug': 'geodezja-w-terenie',
        'image': 'geodezja.jpg',
        'autor': 'Wojtek',
        'date': date(2024, 7, 5),
        'title': 'Geodezja w terenie',
        'excerpt': 'Praca geodety w terenie to nie tylko pomiary, ale również...',
        'content':"""
                {% lorem 5 b random %}
                {% lorem 2 b random %}
        """
    },
    {
        'slug': 'docker-na-vps',
        'image': 'docker.jpg',
        'autor': 'Wojtek',
        'date': date(2025, 1, 20),
        'title': 'Docker na VPS',
        'excerpt': 'Jak skonfigurować kontenery na serwerze VPS i zabezpieczyć je...',
        'content':"""
                {% lorem 3 b random %}
                {% lorem 4 b random %}
        """
    },
]

def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    print(sorted_posts)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def post(request, slug):
    return render(request, 'blog/post-detail.html')
