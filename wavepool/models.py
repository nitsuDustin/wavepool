from django.db import models
from django.urls import reverse

import datetime

DIVESITE_SOURCE_NAMES = {
    'retaildive': 'Retail Dive',
    'ciodive': 'CIO Dive',
    'educationdive': 'Education Dive',
    'supplychaindive': 'Supply Chain Dive',
    'restaurantdive': 'Restaurant Dive',
    'grocerydive': 'Grocery Dive',
    'biopharmadive': 'BioPharma Dive',
    'hrdive': 'HR Dive',
}


class NewsPost(models.Model):
    def __str__(self) -> str:
        return self.title
    
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=3000)
    source = models.URLField()
    is_cover_story = models.BooleanField(default=False)
    publish_date = models.DateField(default=datetime.date.today())

    @property
    def url(self):
        return reverse('newspost_detail', kwargs={'newspost_id': self.pk})

    @property
    def teaser(self):
        return self.body[:150]

    @property
    def source_divesite_name(self):
        return 'Industry Dive'

    def tags(self):
        return [
            'HR', 'Diversity & Inclusion', 'Culture'
        ]
        
    def save(self, *args, **kwargs):
        num_of_cover_story = len(NewsPost.objects.filter(is_cover_story=True))
        if num_of_cover_story == 0:
            return super(NewsPost, self).save(*args, **kwargs)
        else:
            NewsPost.objects.filter(is_cover_story=True).update(is_cover_story=False)
            return super(NewsPost, self).save(*args, **kwargs)
        