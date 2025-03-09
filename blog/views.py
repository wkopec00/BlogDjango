from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

all_posts = [
    {
        'slug':'motorowka-na-mazurach',
        'image':'motorowka.jpg',
        'author':'Wojtek',
        'date': date(2024, 10, 10),
        'title':'Motorówka na mazurach',
        'excerpt':'Pływanie motorówką po jeziorach mazurskich...',
        'content':"""
Mazury to jedno z najpiękniejszych miejsc w Polsce, idealne do żeglugi i wypoczynku nad wodą. Pływanie motorówką po jeziorach mazurskich daje niesamowitą wolność i możliwość eksplorowania ukrytych zatoczek, malowniczych wysepek i cichych przystani. Wiele wypożyczalni oferuje zarówno małe, szybkie łodzie dla amatorów adrenaliny, jak i większe jednostki dla rodzin czy grup przyjaciół.

Podróż motorówką pozwala na szybkie przemieszczanie się między miejscowościami, takimi jak Mikołajki, Giżycko czy Ryn. To świetna alternatywa dla tradycyjnego żeglowania, szczególnie dla tych, którzy wolą silnik od wiatru w żaglach. Jednak warto pamiętać o przepisach i zasadach bezpieczeństwa – zwłaszcza o odpowiednim sprzęcie ratunkowym i dostosowaniu prędkości do warunków na wodzie.
        """
    },
    {
        'slug':'programowanie-jest-super',
        'image':'coding.jpg',
        'author':'Wojtek',
        'date': date(2024, 12, 15),
        'title':'Python jest super',
        'excerpt':'Programowanie w języku Python jest bardzo proste...',
        'content':"""
Język Python od lat cieszy się ogromną popularnością wśród programistów na całym świecie. Jego czytelna składnia, prostota oraz ogromna liczba dostępnych bibliotek sprawiają, że świetnie nadaje się zarówno dla początkujących, jak i do zaawansowanych zastosowań. Wykorzystuje się go w różnych dziedzinach – od analizy danych, przez machine learning, aż po tworzenie aplikacji webowych i automatyzację procesów.

Jedną z największych zalet Pythona jest jego wszechstronność i aktywna społeczność, która stale rozwija język i udostępnia nowe rozwiązania. Frameworki takie jak Django czy Flask umożliwiają szybkie tworzenie aplikacji webowych, a biblioteki jak NumPy i Pandas sprawiają, że analiza danych jest intuicyjna i wydajna. To język, który pozwala skupić się na rozwiązaniu problemu, zamiast na walce z trudną składnią, co czyni go doskonałym narzędziem dla każdego programisty.
        """
    },
    {
        'slug': 'geodezja-w-terenie',
        'image': 'geodezja.jpg',
        'author': 'Wojtek',
        'date': date(2024, 7, 5),
        'title': 'Geodezja w terenie',
        'excerpt': 'Praca geodety w terenie to nie tylko pomiary, ale również...',
        'content':"""
Praca geodety w terenie to znacznie więcej niż tylko pomiary i odczytywanie współrzędnych. To także wyzwania związane z różnorodnym ukształtowaniem terenu, zmieniającymi się warunkami pogodowymi i koniecznością precyzyjnego operowania sprzętem pomiarowym. Nowoczesna geodezja bazuje na zaawansowanych technologiach, takich jak GPS, drony oraz skanery laserowe, które pozwalają na szybkie i dokładne zbieranie danych.

Terenowa część pracy geodety często wymaga dobrej organizacji i współpracy zespołowej. Dokładność pomiarów ma kluczowe znaczenie dla dalszych etapów projektów budowlanych, infrastrukturalnych czy kartograficznych. Właściwe przygotowanie, znajomość narzędzi i umiejętność analizy danych w terenie to cechy, które pozwalają geodetom skutecznie realizować swoje zadania i dostarczać wysokiej jakości wyniki pomiarowe.
        """
    },
    {
        'slug': 'docker-na-vps',
        'image': 'docker.jpg',
        'author': 'Wojtek',
        'date': date(2025, 1, 20),
        'title': 'Docker na VPS',
        'excerpt': 'Jak skonfigurować kontenery na serwerze VPS i zabezpieczyć je...',
        'content':"""
Docker to jedno z najpopularniejszych narzędzi do konteneryzacji aplikacji, które znacząco ułatwia zarządzanie oprogramowaniem na serwerach VPS. Dzięki niemu można uruchamiać aplikacje w odizolowanych środowiskach, eliminując problemy związane z zależnościami i konfiguracją systemową. To świetne rozwiązanie zarówno dla programistów, jak i administratorów, którzy chcą szybko wdrażać i skalować swoje aplikacje.

Konfiguracja Dockera na VPS wymaga kilku kroków, takich jak instalacja silnika Docker, tworzenie obrazów aplikacji oraz zarządzanie kontenerami. W połączeniu z narzędziami takimi jak docker-compose czy Kubernetes, możliwe jest łatwe zarządzanie wieloma usługami i automatyczne ich skalowanie. Dodatkowo, stosowanie reverse proxy (np. Traefik lub Nginx) oraz zabezpieczeń, takich jak firewall i certyfikaty SSL, pozwala na utrzymanie wysokiego poziomu bezpieczeństwa wdrożonych aplikacji.
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
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
