from django.template import loader
from django.http import HttpResponse

from wavepool.models import NewsPost
from wavepool.code_exercise_defs import code_exercise_defs
from django.conf import settings


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            archive: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('wavepool/frontpage.html')
    cover_story = NewsPost.objects.all().order_by('?').first()
    top_stories = NewsPost.objects.all().order_by('?')[:3]
    other_stories = NewsPost.objects.all().order_by('?')

    context = {
        'cover_story': cover_story,
        'top_stories': top_stories,
        'archive': other_stories,
    }

    return HttpResponse(template.render(context, request))


def newspost_detail(request, newspost_id):
    template = loader.get_template('wavepool/newspost.html')
    newspost = NewsPost.objects.get(pk=newspost_id)
    context = {
        'newspost': newspost
    }

    return HttpResponse(template.render(context, request))


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')
    code_exercises = []
    code_reviews = []
    for ce in code_exercise_defs:
        if settings.SENIOR_USER:
            if ce.get('pull_request'):
                code_reviews.append(ce)
            else:
                code_exercises.append(ce)
        else:
            code_exercises = code_exercise_defs
    context = {
        'code_exercise_defs': code_exercises,
        'code_review_defs': code_reviews
    }
    return HttpResponse(template.render(context, request))
