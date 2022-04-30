from django.template import loader
from django.http import HttpResponse

from wavepool.models import NewsPost
from wavepool.code_exercise_defs import code_exercise_defs, code_review_defs, code_design_defs
from django.conf import settings


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            archive: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('wavepool/frontpage.html')
    
    cover_story = None
    top_stories = []
    other_stories = []
    top_story_count = 0
    
    # order newsposts by descending order so we get the lastest post first
    newsposts = NewsPost.objects.all().order_by('-publish_date')
    
    for post in newsposts:
        # check if post is a cover story
        # there doesn't seem to be a cover in the dataset so there will not be a cover story
        if post.is_cover_story == True:
            cover_story = post
        # get the first top 3 stories and append it to the top_stories list
        elif top_story_count < 3:
            top_stories.append(post)
            top_story_count += 1
        # append all other stories that are not cover or top stories into the other_stories list
        else:
            other_stories.append(post)
        
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

    context = {
        'code_exercise_defs': code_exercise_defs,
        'code_design_defs': code_design_defs,
        'code_review_defs': code_review_defs,
        'show_senior_exercises': settings.SENIOR_USER,
    }
    return HttpResponse(template.render(context, request))
