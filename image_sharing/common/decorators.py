from django.http import HttpResponseBadRequest
import functools


def ajax_required(f):
    @functools.wraps(f)
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    return wrap
