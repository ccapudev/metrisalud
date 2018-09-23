from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render


class Exceptions(MiddlewareMixin):

    def process_exception(self, request, exception):
        if request.is_ajax():
            from django.http import JsonResponse
            return JsonResponse(dict(
                error=str(exception),
            ), status=400)
        else:
            exception = str(exception)
            return render(request, 'errors/400.html', locals(), status=400)

