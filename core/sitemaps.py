from django.contrib.sitemaps import Sitemap
from core import models
from django.urls import reverse


class AnimalSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return models.Animal.objects.exclude(state='UNAVAILABLE').order_by('-state', 'entry_date')

    def lastmod(self, obj):
        return obj.modified


class HomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return models.Animal.objects.filter(state='URGENCY').order_by('-state', 'entry_date')

    def lastmod(self, obj):
        return obj.modified


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['frequentQuestions', 'aboutUs', 'help', 'contact']

    def location(self, item):
        return reverse(item)
