from .models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url #{'LINK_TWITTER': 'twitter.com','LINK_FACEBOOK': 'facebook.com'}
    return ctx
